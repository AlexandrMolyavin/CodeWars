https://www.codewars.com/kata/5426d7a2c2c7784365000783

s= []
def parens(l, r, str):
    if l == 0 and r == 0:
        s.append(str)
    if l > 0:
        parens(l-1, r+1, str+"(")
    if r > 0:
        parens(l, r-1, str+")")

def balanced_parens(n):
    s.clear()
    parens(n, 0, '')
    s.reverse()
    return s