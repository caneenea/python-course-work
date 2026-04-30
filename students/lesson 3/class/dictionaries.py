d_example = {'key1' : 'val1'}

d1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}

print(d1)
print(d1.keys())
print(d1.values())
print(d1['a'])

d1['e'] = 5 #add last
print(d1)
print(d1.keys())
print(d1.values())

d1['a']= 200 #change element
print(d1)
print(d1.keys())
print(d1.values())

print(d1.get('e'))
print(d1.get('z')) #if it does not exist = NONE

d2 = {

    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4,
    'e' : [1,2,3,4]


}

print(d2)

d3 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}

print(d3)
print(d3.keys())
print(d3.values())
print(d3.items())
