""""
Build a function that takes from the user a number n and prints a Triangle with stars, print should not print more than 1 character
"""""
def build_TR(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end=" ")
        print()

n = int(input("Enter a number: "))
build_TR(n)
