def pattern(n):
    # Happy Coding ^_^
    if n <= 0: return ""
    a = ""
    flag = False
    i = 1
    while i != n+1:
        a += str(i)
        i+=1

    b = a + "\n"
    while a != str(n):
        if a[0] == '1' and a[1] == '0':
            flag = True
        if flag == False:
            a = a[1:]
        else:
            a = a[2:]
        b += a + "\n"
    return b[:-1]