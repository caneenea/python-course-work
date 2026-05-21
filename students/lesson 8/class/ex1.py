"""
Build a function that takes 2 list and add elements

"""
"""
my solution
"""

def add(a, b):
    c=[]
    if len(a) != len(b):
        if len(a) > len(b):
            for i in range(len(b)):
                c.append(a[i] + b[i])
            return c
        elif len(a) < len(b):
            for i in range(len(a)):
                c.append(a[i] + b[i])
            return c
    for i in range(len(a)):
            c.append(a[i]+b[i])
    return c

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = [1,2,3,4,5]

print(add(list1, list2))
print(add(list1, list3))
