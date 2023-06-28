with open("C:/CookAnalysis/CSV/singer1.csv", "r") as inFp :
    with open("C:/CookAnalysis/CSV/new_singer2_0628.csv", "w") as outFp:
        #해더
        header = inFp.readline()
        header = header.strip()
        header_list= header.split(',')


        idx1 = header_list.index('아이디')  #0
        idx2 = header_list.index('이름') #1
        idx3 = header_list.index('평균 키') #7

        header_list = [header_list[idx1], header_list[idx2], header_list[idx3]]
        header_str = ','.join(map(str, header_list))
        outFp.write(header_str + '\n')

        #데이터 쓰기작업, 2번째 행부터
        for inStr in inFp:
            inStr = inStr.strip()
            row_list = inStr.split(',')
            if int(row_list[idx3]) >= 165 :
                row_list = [row_list[idx1], row_list[idx2], row_list[idx3]]
                row_str = ','.join(map(str, row_list))
                outFp.write(row_str + '\n')

print('Save. OK~')