#Build a function where you take a number and check if palindrome

def palindrome(num):
    count = 0
    lst = []
    while num > 0:
        digit = num % 10
        lst.append(digit)
        num = num // 10
    n1 = len(lst) - 1
    for i in range(n1 // 2):
        if lst[i] != lst[n1 - 1 - i]:
            print("Not a palindrome")
        else :
            print("Palindrome")












palindrome(1234321)
