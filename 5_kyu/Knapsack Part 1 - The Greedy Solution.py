https://www.codewars.com/kata/53ffbba24e9e1408ee0008fd
def knapsack(capacity, items):
    # Be greedy!
    r = [0 for i in range(len(items))]
    found = True
    while found:
        found = False
        i_max = -1
        best_ratio = 0
        for i in range(len(items)):
            size, value = items[i]
            ratio = float(value) / size
            if size <= capacity and ratio > best_ratio:
                i_max = i
                best_ratio = ratio
                found = True
        if found:
            r[i_max] += 1
            capacity -= items[i_max][0]
    return r
