def divisible_by(numbers,divisor  ):
    a = []
    for item in numbers:
        if item % divisor == 0:
            a.append(item)
    return a