def equable_triangle(a,b,c):
    p = (a +b +c)/2
    s = (p*(p-a)*(p-b)*(p-c))
    s = s**0.5
    return True if s ==p*2 else False
    
    #your code here
