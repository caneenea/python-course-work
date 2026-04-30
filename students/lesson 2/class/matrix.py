lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [7, 8, 9, [10,11]]

matrix = [lst1, lst2, lst3]
print(matrix)
print(matrix[2][3][:2])

#pop and reverse can be done, sort cant when you have ints and lists inside a list

matrix[2][3].pop()
print(matrix)

