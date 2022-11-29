https://www.codewars.com/kata/5a405ba4e1ce0e1d7800012e
def custom_christmas_tree(chars, n):
    leaveptr = 0
    tree = ""
    for row in range(n):
        rowstr = ""
        if row != 0:
            rowstr += "\n"
        for i in range(1, n - row - 1):
            rowstr += " "
        for i in range(row + 1):
            if row != n - 1 or i != 0:
                rowstr += " "
            rowstr += chars[leaveptr]
            leaveptr += 1
            leaveptr %= len(chars)

        tree += rowstr

    trunkstr = ""

    for i in range(n - 1):
        trunkstr += " "
    trunkstr += "|"

    for i in range(n // 3):
        tree += "\n" + trunkstr
    return tree
