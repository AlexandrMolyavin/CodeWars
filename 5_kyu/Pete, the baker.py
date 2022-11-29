https://www.codewars.com/kata/525c65e51bf619685c000059
def cakes(recipe, available):
    for item in recipe:
        if item not in available:
            return 0
    res = 0
    min_res = float("inf")
    for item1 in recipe:
        for item2 in available:
            if item1 == item2:
                while available[item2] - recipe[item1] >= 0:
                    available[item2] -= recipe[item1]
                    res+=1
                break
        if res<min_res:
            min_res = res
        res = 0

    return min_res
