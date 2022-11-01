def well(x):
    #your code here
    i = 0
    for item in x:
        if item == 'good':
            i+=1
    if i == 0:
             return 'Fail!'
    if i == 1 or i == 2:
                return 'Publish!'
    if i > 2:
                return 'I smell a series!'