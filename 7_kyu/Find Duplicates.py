def duplicates(array):
    l1=[]
    duplist = []
    for item in array:
        if item not in l1:
            l1.append(item)
        else:
            if item not in duplist:
                duplist.append(item)
    return duplist



