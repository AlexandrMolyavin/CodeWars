def no_odds(values):
    # Return list of only even values
    a = []
    for item in values:
        if item%2 == 0:
            a.append(item)
    return a
