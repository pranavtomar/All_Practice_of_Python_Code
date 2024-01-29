def nearest_palindrome(number):
    #start writitng your code here
    number += 1
    while True:
        num = number
        pal = 0
        while num > 0:
            rem = num % 10
            pal = pal * 10 + rem
            num //= 10
        if pal == number:
            return pal
        else:
            number += 1

number=12331
print(nearest_palindrome(number))

