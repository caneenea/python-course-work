#u4
#build a function that  creates a list from the elements that the user gives, the user has to press exit for the programm to stop

def create_list():
    lst = []
    while True:
        x = input()

        if x == "exit":
            break
        x = int(x)
        lst.append(x)
    return(lst)

lst1 = create_list()
print(lst1)
