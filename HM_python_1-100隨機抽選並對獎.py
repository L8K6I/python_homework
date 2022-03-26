# -*- coding: utf-8 -*-

count = 0
data = []
for i in range(6):
    guess = int(input("請輸入數字(不重複)："))
    data.append(guess)
    count += 1
    if count == 6:
        print("已猜完6個數字")         

import random  
# for i in range(1,101):
    # print(i,end = ",")
data2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
a = []
for i in range(6):
    n = random.randint(0,len(data2)-1)
    num = data2.pop(n)
    a.append(num)
    print("系統選號:",num)

print("系統選號:",a)
print("你猜選的號碼",data)    

for g in range(6):
    if (a == data): 
        count <= 6
        print("恭喜中獎",count,"個號碼獲得",(count*10)-10,"顆蘋果")
    else:
        print("再接再厲")
        break
    

        


