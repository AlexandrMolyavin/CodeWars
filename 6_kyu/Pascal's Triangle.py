def pascals_triangle(n):
    if n < 1:
        return None
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1, 1]
    r = [1, 1, 1]
    prev_row = [1, 1]
    for i in range(3, n + 1):
        row = [1] + [0 for j in range(1,i-1)] + [1]
        for j in range(1, i - 1):
            row[j] = prev_row[j-1] + prev_row[j]
        r += row
        prev_row = row
    return r
