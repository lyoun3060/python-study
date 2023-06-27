i = 0
hap = 0
check = []

for i in range(1, 11, 1) :
     hap = hap + i
     check.append(hap)
     
print(check)

print("1에서 10까지의 합계 : %d" % hap)
