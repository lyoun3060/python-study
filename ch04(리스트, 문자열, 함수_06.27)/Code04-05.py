list1 = []
list2 = []
value=1
for i in range(0, 3) :
    for k in range(0, 4) :
        list1.append(value)
        value += 1
    list2.append(list1)
    list1 = []
    #list2에는 int값 하나가 들어가는게 아니라 배열이 들어감

for i in range(0, 3) :
    for k in range(0, 4) :
        print("%3d" % list2[i][k], end = " ")
    print("")
