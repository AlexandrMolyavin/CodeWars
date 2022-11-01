def search_names(logins):
    pass
    a = []
    for item1 in logins:
        for item2 in item1:
            if item2[len(item2)-1]=='_':
                a.append(item1)
    return a   
