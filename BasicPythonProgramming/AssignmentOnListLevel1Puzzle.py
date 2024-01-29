def check_perfect_number(number):
    if (number == 0):
        return False
    sum = 0
    for divisor in range(1,number):
        if number % divisor == 0:
            sum += divisor
    if sum == number:
        return True
    return False

def check_perfectno_from_list(no_list):
    perfect_no_list = []
    for num in no_list:
        if(check_perfect_number(num) == True):
            perfect_no_list.append(num)
    return perfect_no_list

perfectno_list = check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)
