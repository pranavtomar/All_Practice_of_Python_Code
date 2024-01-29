stNo = int(input())
endNo = int(input())

for i in range(stNo,endNo+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i,end=" ")