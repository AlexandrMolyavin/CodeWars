def check_tombola(sheet):
    if [len(row) for row in sheet] != [9,9,9]:
        return False
    if [len(set(row) - set([0])) for row in sheet] != [5,5,5]:
        return False

    for i in range(9):
        col = [sheet[0][i], sheet[1][i], sheet[2][i]]
        col_nonzero = [c for c in col if c != 0]
        
        if col.count(0) == 3:
            return False
        if col_nonzero != sorted(col_nonzero) or len(col_nonzero) != len(set(col_nonzero)):
            return False
        
        for num in col_nonzero:
            if i < 8 and num not in range(10*i,10*i+10):
                return False
            elif i == 8 and num not in range(80,91):
                return False 
    return True
