#filter
def even(num):
    if num % 2 == 0:
     print("even")

list1 = [1,2,3,4,5,6]
list2 = filter(even, list1)
print(list2) #prints object
list3 = list(filter(even, list1))
print(list3)

#lambda
lambda n: n % 2 == 0

list4= list(filter(lambda n: n % 2 == 0, list1))
print(list4)

#map

list5=list(map(lambda n: n*n, list1))
print(list5)

