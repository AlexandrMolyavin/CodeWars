def generate_range(min, max, step):
    a = []
    while min <= max:
        a.append(min)
        min += step
    return a
