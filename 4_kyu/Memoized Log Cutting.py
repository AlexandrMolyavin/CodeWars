https://www.codewars.com/kata/54b058ce56f22dc6fe0011df

def cut_log(p, n):
    r = [0] * (n + 1)
    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            q = max(q, p[i] + r[j-i])
        r[j] = q
    return r[n]