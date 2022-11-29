https://www.codewars.com/kata/5b5f7f7607a266914200007c
def combs_non_empty_boxes(n, k):
    # your code here
    if n < k: return "It cannot be possible!"
    row = [1] + [0 for _ in range(k)]
    for i in range(1, n + 1):
        new = [0]
        for j in range(1, k + 1):
            stirling = j * row[j] + row[j - 1]
            new.append(stirling)
        row = new
    return row[k]

# n: amount of elements of the sets
# k: amount of equal boxes
# combs: amount of combinations of elements with non empty boxes
