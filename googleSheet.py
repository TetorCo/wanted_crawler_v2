import datetime
import gspread
import time
from collections import Counter

gc = gspread.service_account(filename='/Users/taebeomkim/wanted_crawler_v2/stable-victory-376907-a8e79002c478.json')
doc = gc.open_by_url("https://docs.google.com/spreadsheets/d/19tQxXwZJpOJ43-IWeoh1AACfRcEb3_mPFnNid7XmGxA/edit?usp=sharing")


def sheetWrite(sheetName, data):  # 구글 시트에 데이터를 입력하는 함수입니다.

    doc.worksheet(f"{sheetName}").append_rows(data, insert_data_option='INSERT_ROWS')


def sheetReadMain(sheetName):  # 구글 시트에 입력되있는 회사명과 공고 이름을 가져오는 함수입니다.

    sheetData = doc.worksheet(f"{sheetName}").get_all_records()
    existJD = []

    if sheetData == []:
        ...
    else:
        for i in sheetData:
            existJD.append(list(i.values())[:2])

    return existJD


def stackSheetReadAndWrite(sheetName, data):
    ## 직무 별 기술스택을 월 별로 기입하는 함수입니다.

    stackColList = doc.worksheet(f'{sheetName}').col_values(1)
    print(stackColList)

    month = datetime.date.today().month

    for rowData in data:

        if list(rowData)[0] in stackColList: ...
        else:
            doc.worksheet(f'{sheetName}').insert_row([f'{list(rowData)[0]}'], len(stackColList)+1)
            stackColList.append(list(rowData)[0])
    
        cell = doc.worksheet(f'{sheetName}').find(f'{list(rowData)[0]}')
        # print(f'{list(rowData)[0]}의 위치는 {cell.row}, {cell.col}')
        doc.worksheet(f'{sheetName}').update_cell(cell.row, cell.col+month, list(rowData)[1])
        time.sleep(2)


def extractStack(name, data):
    ## 구글 시트에 기술스택을 입력하기 위해서 카운트를 하는 함수입니다.

    stackList = list()

    data = [i['기술스택 ・ 툴'] for i in data]

    for i in data:
        x = i.split('\n')
        stackList.extend(x)

    stackList = [i for i in stackList if i]
    stackList = Counter(stackList).most_common(20)
    print(f'{name}의 기술 스택 결과 : {stackList}')

    stackSheetReadAndWrite(name, stackList)