def solution(mtrx):
    for i in range(len(mtrx)):
        for j in range(len(mtrx)):
            if mtrx[i][j] == '^':
                for k in range(0,i):
                    if mtrx[k][j] == 'x':
                        return True
                return False
            elif mtrx[i][j] == '>':
                if 'x' in mtrx[i][j+1:]:
                    return True
                else:
                    return False
            elif mtrx[i][j] == '<':
                if 'x' in mtrx[i][0:j]:
                    return True
                else:
                    return False
            elif mtrx[i][j] == 'v':
                for k in range(i+1,len(mtrx)):
                    if mtrx[k][j] == 'x':
                        return True
                return False