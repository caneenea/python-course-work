# Build a function that finds the sum of the digits of a number

def sumDigits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    print(total)


n = int(input("Enter a number: "))
sumDigits(n)