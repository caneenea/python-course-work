from copy import deepcopy

d1 = {'a' : 1, 'b' : 2, 'c' : 3}
d2 =d1.copy()
d3 = deepcopy(d1)
print(d2)
print(d1)
print('1', '_'*40)
d1['d'] = 4
d2['e'] = 5
print(d2)
print(d1)
print(d3)
print('2', '_'*40)
