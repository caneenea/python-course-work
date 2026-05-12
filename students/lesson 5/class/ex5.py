#u5
#Build a function that takes from the user a list and returns the sum of the even elements

def lists(lengthOflist):
    lst = []
    sum = 0
    for i in range(lengthOflist):
        x = int(input())
        lst.append(x)
        if x % 2 == 0:
            sum = sum + x

    return sum


l1 = lists(int(input('The length of the list is = ')))
print(l1)