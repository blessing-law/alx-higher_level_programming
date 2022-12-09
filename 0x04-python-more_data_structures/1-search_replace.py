#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = list(my_list)
    for i in my_list:
        if i == search:
            newList[j] = replace
        j += 1
    return newList
