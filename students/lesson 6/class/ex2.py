#Build a function that takes from the user a number n and prints a square with stars, print should not print more than 1 character
def print_sq(n):
 print("The square is : ")

 for i in range(n):
    for j in range(n):
      print("*", end=" ")
    print()


n = int(input('Enter the number = '))
print_sq(n)