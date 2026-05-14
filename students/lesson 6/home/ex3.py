# Build a function that counts positive, negative, and zero numbers

def countNumbers(n):
    positive = 0
    negative = 0
    zero = 0

    for i in range(n):
        num = int(input("Enter a number: "))

        if num > 0:
            positive = positive + 1
        elif num < 0:
            negative = negative + 1
        else:
            zero = zero + 1

    print("Positive numbers:", positive)
    print("Negative numbers:", negative)
    print("Zero:", zero)


n = int(input("How many numbers do you want to enter? "))
countNumbers(n)