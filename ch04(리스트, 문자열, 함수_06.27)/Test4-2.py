check1 = []
check2 = []
value = 0

for i in range(0,4):
    for i2 in range(0, 5):
        check1.append(value)
        value+=3
    check2.append(check1)
    check1 = []

for i3 in range(0,4):
    print(check2[i3])
    print("")


    