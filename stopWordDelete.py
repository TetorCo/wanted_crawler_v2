def sentenceTokenizing(crawlingData):

    retokenize = RegexpTokenizer("\w+")
    totalWordList = []
    totalStackList = []
    cnt = 0

    with open(crawlingData, 'r') as file:
        files = csv.reader(file)

        for idx, rowData in enumerate(files):
            if idx == 0:
                ...
            else:
                cnt += 1
                # print(rowData[4])
                # print(re.split('\n', rowData[4]))
                tempSentence = re.split('\n', rowData[4])

                for sentence in tempSentence:
                    retoken = retokenize.tokenize(sentence)
                    # print(f'nltk : {retoken}')

                    for wordToken in retoken:

                        if wordToken.upper() == wordToken.lower():  # 한글일 경우
                            mecabFilter = mecab.nouns(wordToken)
                            # print(f'Mecab : {mecabFilter}')  # -> List Type
                            if mecabFilter == []: ...
                            else: totalWordList.extend(mecabFilter)
                        else:
                            # print(wordToken)
                            totalWordList.append(wordToken)

                tempStack = re.split('\n', rowData[-1])
                totalStackList.extend(tempStack)
    # print(totalWordList)
    print(Counter(totalWordList).most_common(50))
    print(Counter(totalStackList).most_common(21))
    print(f'총 공고 개수는 {cnt}개')


if __name__ == "__main__":

    import csv
    import konlpy
    import re
    import nltk
    from nltk.tokenize import RegexpTokenizer
    from konlpy.tag import Mecab
    from collections import Counter
    import jdLink

    mecab = Mecab()

    # path = 'crawlingData/2023-04-13 16:53:22_wanted_crawling.csv'
    dsPath = 'crawlingData/2023-04-20 12:09:27_ds_wanted_crawling.csv'
    daPath = 'crawlingData/2023-04-22 17:03:31_da_wanted_crawling.csv'
    dePath = 'crawlingData/2023-04-22 17:22:49_de_wanted_crawling.csv'
    mlePath = 'crawlingData/2023-04-22 17:57:28_mle_wanted_crawling.csv'

    # sentenceTokenizing(dsPath)
    # sentenceTokenizing(daPath)
    # print()
    # sentenceTokenizing(dePath)
    # print()
    # sentenceTokenizing(mlePath)
    # print()


    with open(mlePath, 'r') as file:

        data = csv.reader(file)
        
        for idx, rowData in enumerate(data):
            
            emptyList = []
            if idx == 0: ...
            # if idx > 5: break
            else:
                # print(rowData)
                tempList = rowData[4:5]
                for i in tempList:
                    # print(type(i))
                    words = re.split('\n', i)
                    # print(words)
                    for j in words:
                        word = re.split('[],(,[, -, _, /, ), ㆍ]', j)
                        # print(word)
                        if '분석' in word:
                            # print("===============================================")
                            # print(rowData[0], rowData[1], rowData[-2], j)
                            # print(rowData[0])
                            # print(rowData[1])
                            # print(rowData[-2])
                            print(j)
                            # print("===============================================")


    # with open(daPath, 'r') as file:

    #     data = csv.reader(file)
        
    #     for idx, rowData in enumerate(data):
            
    #         emptyList = []
    #         if idx == 0: ...
    #         # if idx > 5: break
    #         else:
    #             tempList = rowData[4:5]
    #             for i in tempList:
    #                 # print(type(i))
    #                 words = re.split('\n', i)
    #                 # print(words)
    #                 for j in words:
    #                     word = re.split('[],(,[, -, _, /, ), ㆍ]', j)
    #                     # print(word)
    #                     if '개발' in word:
                            # print("===============================================")
                            # print(rowData[0], rowData[1], rowData[-2], j)
                            # print(rowData[0])
                            # print(rowData[1])
                            # print(rowData[-2])
                            # print(j)
    #                         print("===============================================")

    #     daCntList = []
    #     deCntList = []
    #     dsCntList = []
    #     mleCntList = []
    #     checkList = []
        
    #     da = 0
    #     de = 0
    #     ds = 0
    #     mle = 0


    #     for idx, rowData in enumerate(files):
    #         cnt = 0
    #         print(rowData[1])

    #         words = re.split('[],(,[, -, _, /, )]', rowData[1])
    #         words = [i.lower() for i in words]
    #         words = ' '.join(words).split()

    #         for word in words:

    #             if word in jdLink.daFilter:
    #                 cnt += 1
            # tempList = rowData[4].split('\n')

            # for temp in tempList:
            #     # temp = re.split('[],(,[, -, _, /, )]', temp)
            #     print(temp)
            #     print()
            #     # print(f'Mecab : {mecab.nouns(temp)}')
            #     retokenize = RegexpTokenizer("\w+")
            #     retoken = retokenize.tokenize(temp)
            #     print(f'nltk: {retoken}')
            #     # tokens = nltk.word_tokenize(temp)
            #     # print(f'nltk : {tokens}')
            #     # extendList.extend(retoken)
            #     # print(extendList)

            #     # print(f'Okt : {okt.nouns(temp)}')
            #     # print(f'Kkma : {kkma.nouns(temp)}')
            #     print()
            # if idx == 5: break
        # str = ' '.join(extendList)
        # print(str)
        # print(mecab.nouns(str))
        # test = 'task를'
        # print(test.upper())
        #     job = {
        #     'daCnt' : 0,
        #     'dsCnt' : 0,
        #     'deCnt' : 0,
        #     'mleCnt' : 0
        #     }

        #     if idx == 0: ...
        #     else:

        #         words = re.split('[],(,[, -, _, /, )]', rowData[1])
        #         words = [i.lower() for i in words]
        #         words = ' '.join(words).split()
        #         # print(words, rowData[1].lower())

        #         for word in words:

        #             if word in jdLink.daFilter:
        #                 job['daCnt'] += 1
        #             if word in jdLink.deFilter:
        #                 job['deCnt'] += 1
        #             if word in jdLink.dsFilter:
        #                 job['dsCnt'] += 1
        #             if word in jdLink.mleFilter:
        #                 job['mleCnt'] += 1
                
        #             # print(daCnt, deCnt, dsCnt, mleCnt)
        #         for key, value in job.items():
        #             if max(job.values()) == value:
        #                 eval(key+'List').extend(mecab.nouns(rowData[4]))

        #                 if key == 'daCnt': da += 1
        #                 elif key == 'deCnt': de += 1
        #                 elif key == 'dsCnt': ds += 1
        #                 else: mle += 1
        
        # print(f'da:{da}, de:{de}, ds:{ds}, mle:{mle}')
        # print(Counter(daCntList).most_common(50))
        # print(Counter(deCntList).most_common(50))
        # print(Counter(dsCntList).most_common(50))
        # print(Counter(mleCntList).most_common(50))