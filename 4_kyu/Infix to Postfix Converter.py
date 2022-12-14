https://www.codewars.com/kata/52e864d1ffb6ac25db00017f

def to_postfix(infix):
    stack = []
    output = ""
    op = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
    ro = {'^': 2}
    for x in infix:
        if x.isdigit():
            output += x
        elif x == "(":
            stack.append(x)
        elif x in ro:
            stack.append(x)
        elif x in op:
            while stack and stack[-1] != '(':
                if op[x] <= op[stack[-1]]:
                    output += stack.pop()
                else:
                    break
            stack.append(x)
        elif x == ")":
            while stack[-1] != '(':
                output += stack.pop()
            stack.pop()

    return output + "".join(stack[::-1])