https://www.codewars.com/kata/5672682212c8ecf83e000050

def dbl_linear(n):
    qx = []
    qy = []
    q = [1]
    for i in range(1, n + 1):
        x = q[-1]
        qx.append(2 * x + 1)
        qy.append(3 * x + 1)
        if qx[0] < qy[0]:
            q.append(qx.pop(0))
        elif qx[0] == qy[0]:
            q.append(qx.pop(0))
            qy.pop(0)
        else:
            q.append(qy.pop(0))
    return q[-1]