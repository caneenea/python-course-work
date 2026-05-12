#u3
#Nderto nje funksion i cili krijon nje liste me numra int te dhenat nga perdorusi

def lists(lengthOflist):
    lst = []
    for i in range(lengthOflist):
        x = int(input())
        lst.append(x)
    print(lst)


lists(int(input('The length of the list is = ')))

