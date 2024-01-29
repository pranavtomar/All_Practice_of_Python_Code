def factorial(number):
    fact = 1
    while number > 0: #remove pass and write your logic to find and return the factorial of given number
        fact *= number
        number -= 1
    return fact

def find_strong_numbers(num_list):
    new_num_list = [] #remove pass and write your logic to find and return the list of strong numbers from the given list
    for number in num_list:
        if number == 0:
            break
        sum = 0
        num = number
        while num > 0:
            rem = num % 10
            sum += factorial(rem)
            num //= 10
        if number == sum:
            new_num_list.append(number)
    return new_num_list

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)