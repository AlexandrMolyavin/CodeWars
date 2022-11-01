def check_exam(arr1,arr2):
    score = 0
    for i1,item1 in enumerate(arr1):
        for i2,item2 in enumerate(arr2):
            if i1 == i2 : 
                if item1 == item2:
                    score+=4
                    break
                if (item2 != item1) and (item2 != ""):
                    score-=1
                    break
    return score if score>0 else 0
