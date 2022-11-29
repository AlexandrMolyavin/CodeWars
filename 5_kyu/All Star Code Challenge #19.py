from itertools import permutations

def slogan_maker(array):
    #your code here
    arr=[]
    for item in array:
        if not item in arr:
            arr.append(item)
    if len(arr)==1:
        return arr
    arr=list(permutations(arr))
    res=[]
    for j in range(len(arr)):
        tmp=''
        for i in range(len(arr[0])):
            tmp=tmp+' '+arr[j][i]
        res.append(tmp[1:])
    return res