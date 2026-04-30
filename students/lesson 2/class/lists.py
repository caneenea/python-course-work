lst = [1,2,3,4,5]
print(lst)

lst1 = ["a",2,"b",4,"c"]
print(lst1)
print(lst1[-1])
print(lst1[1:5])
print(lst1[1:])
print(lst1[5:5])
print(lst1[::-1])

lst3 = lst1 + lst
print(lst3)
lst3 = lst1 * 2
print(lst3)

print(type(lst3))
print(type(lst3[0]))
print(type(lst3[1]))

lst.append(6) #it gets appended in the end
print(lst)

lst.insert(1,7) #gets appended in the index
print(lst)

lst.pop() #removes the last
print(lst)

lst.remove(4) #removes the element of said index
print(lst)

lst.reverse()
print(lst)

lst.append(4)
lst.append(6)
print(lst)

lstS = sorted(lst) #does not change the actual list
print(lstS)
