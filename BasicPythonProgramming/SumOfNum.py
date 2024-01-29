str = input("Enter a numeric string with comma:\n")
list = str.split(",")
print(list)
sum = 0
flag = 1
for num in list:
    for ch in num:
        if not(ch.isdigit() or ch == '-'):
            flag = 0
            break
    if flag == 0:
        sum = 0
        print("Not Convertable format charaters Sum =",end="")
        break
    sum += int(num)
print(sum)

