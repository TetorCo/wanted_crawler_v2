import re

totalUrl = {
    # 'ds': [
    #     'https://www.wanted.co.kr/search?query=%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%82%AC%EC%9D%B4%EC%96%B8%ED%8B%B0%EC%8A%A4%ED%8A%B8',
    #     'https://www.wanted.co.kr/search?query=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%82%AC%EC%9D%B4%EC%96%B8%ED%8B%B0%EC%8A%A4%ED%8A%B8',
    #     'https://www.wanted.co.kr/search?query=data%20scientist',
    #     'https://www.wanted.co.kr/search?query=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EA%B3%BC%ED%95%99%EC%9E%90'
    #     ],
    'da': [
        'https://www.wanted.co.kr/search?query=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EB%B6%84%EC%84%9D%EA%B0%80',
        'https://www.wanted.co.kr/search?query=data%20analyst',
        'https://www.wanted.co.kr/search?query=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%95%A0%EB%84%90%EB%A6%AC%EC%8A%A4%ED%8A%B8'
        ],
    'de': [
        'https://www.wanted.co.kr/search?query=%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4',
        'https://www.wanted.co.kr/search?query=data%20engineer',
        'https://www.wanted.co.kr/search?query=%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4'
        ],
    'mle' : [
        'https://www.wanted.co.kr/search?query=ML',
        'https://www.wanted.co.kr/search?query=machine%20learning',
        'https://www.wanted.co.kr/search?query=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D',
        'https://www.wanted.co.kr/search?query=deep%20learning',
        'https://www.wanted.co.kr/search?query=%EB%94%A5%EB%9F%AC%EB%8B%9D',
        'https://www.wanted.co.kr/search?query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5'
        ]
}

filter = ['data', '데이터', '빅데이터', '엔지니어', 'Engineer', '데이터엔지니어', 'mlops', '분석가', 'analyst', '데이터분석가', '애널리스트', 'ai', '인공지능', '과학자', '연구원',
'researcher', 'scientist', 'ml', 'dl', '머신러닝', '딥러닝', 'machine', 'deep', 'backend', '데이터사이언티스트', '데이터분석', '인공지능데이터']

# daFilter = ['data', 'analyst', '데이터', '빅데이터', '데이터분석', '데이터분석가', '분석가', '분석팀', '애널리스트', '분석', '데이터분석팀']
# deFilter = ['data', '데이터', '빅데이터', '엔지니어', 'engineer', '데이터엔지니어', 'mlops', '빅데이터엔지니어', 'db', 'db엔지니어', '데이터베이스', 'database']
# dsFilter = ['data', '데이터', '빅데이터', '과학자', '연구원', 'researcher', 'scientist', '데이터사이언티스트', '사이언티스트', 'ml', 'dl', '머신러닝', '딥러닝', 'machine', 'deep', 'learning', 'ai', '인공지능']
# mleFilter = ['data', '데이터', '빅데이터', '머신러닝 엔지니어', '머신러닝엔지니어', 'ml', 'dl', '머신러닝', '딥러닝', 'machine', 'deep', 'learning', 'ai', '인공지능']

daFilter = ['analyst', '데이터분석', '데이터분석가', '분석가', '분석팀', '애널리스트', '분석', '데이터분석팀']
deFilter = ['엔지니어', 'engineer', '데이터엔지니어', 'mlops', '빅데이터엔지니어', 'db', 'db엔지니어', '데이터베이스', 'database']
dsFilter = ['과학자', '연구원', 'researcher', 'scientist', '데이터사이언티스트', '사이언티스트', 'ml', 'dl', '머신러닝', '딥러닝', 'machine', 'deep', 'learning', 'ai', '인공지능']
mleFilter = ['머신러닝 엔지니어', '머신러닝엔지니어', 'ml', 'dl', '머신러닝', '딥러닝', 'machine', 'deep', 'learning', 'ai', '인공지능']


def jobClassification(category, jobName):

    result = False
    cnt = 0

    words = re.split('[],(,[, -, _, /, )]', jobName)
    words = [i.lower() for i in words]
    words = ' '.join(words).split()

    for word in words:

        if word in eval(category+'Filter'):
            cnt += 2

    if cnt >= 2:
        result = True

    elif '데이터사이언티스트' in words:
        if category == 'ds':
            result = True
    elif '데이터엔지니어' in words:
        if category == 'de':
            result = True
    elif '데이터분석가' in words:
        if category == 'da':
            result = True


    return result


if __name__ == "__main__":

    testDe = ['데이터엔지니어']

    if '데이터사이언티스트' in testDe or '데이터엔지니어' in testDe or '데이터분석가' in testDe:
        print(True)

    # import csv

    # path = 'crawlingData/2023-04-13 16:53:22_wanted_crawling.csv'

    # with open(path, 'r') as file:

    #     files = csv.reader(file)
    #     # files = next(files)

    #     for idx, rowData in enumerate(files):
            
    #         if idx == 0: ...
    #         else: print(rowData[0], rowData[4])
    #         # break