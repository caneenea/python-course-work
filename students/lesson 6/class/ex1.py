#Build a function that finds the biggest element in a dict

#MySolution
def findBiggest(d1):
 max = d1['a']
 for key in d1.keys():
    if max < d1[key]:
        max = d1[key]
 print(max)

d1 = {'a' : 12, 'b' : 7, 'c' : 300, 'd' : 4}
findBiggest(d1)

#ProfessorSolution

def findMax(dct):
    max = -9999
    for el in dct.values():
        if max < el:
            max = el
    print(max)

d2 = {'a' : 12, 'b' : 700, 'c' : 300, 'd' : 4}
findMax(d2)



