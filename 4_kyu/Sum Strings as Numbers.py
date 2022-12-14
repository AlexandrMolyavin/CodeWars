https://www.codewars.com/kata/5324945e2ece5e1f32000370

def sum_strings(x, y):
    result = ''
    flag = 0

    if x == '': x = '0'
    if y == '': y = '0'
    if len(y) > len(x):
        x = '0' * (len(y) - len(x)) + x
    else:
        y = '0' * (len(x) - len(y)) + y

    for i in range(len(x) - 1, -1, -1):
        sum_digit = (int(x[i]) + int(y[i]) + flag) % 10
        flag = (int(x[i]) + int(y[i]) + flag) // 10
        result += str(sum_digit)
    result = result[::-1]

    if flag == 1:
        result = '1' + result
    else:
        if result[0] == '0' and len(result) > 1:
            result = result[1::]

    return result