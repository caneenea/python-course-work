def remove_dupes(list):
    i = 0
    j = i + 1
    for i in list:
        for j in list:
            if list[i] == list[j]:
                list.remove(j)
                print(list)

    print(list)

lst1 = [1,1,2,2,2,3,4,4]
remove_dupes(lst1)
