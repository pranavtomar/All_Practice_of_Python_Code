num = int(input("Enter a Number:\n"))
if num < 2:
    print("Not prime")
else:
    flag = 1
    for i in range(2,num):
        if num % i == 0:
            flag = 0
            break
    if flag == 1:
        print("Prime")
    else:
        print("Not Prime")


