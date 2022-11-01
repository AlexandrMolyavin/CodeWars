def boredom(staff):
    #your code here
    sum = 0
    b = {"accounts" :1,
        "finance" : 2,
        "canteen" : 10,
        "regulation" : 3,
        "trading" : 6,
        "change" : 6,
        "IS" : 8,
        "retail" : 5,
        "cleaning" : 4,
        "pissing about" : 25}
    a = staff.values()
    for item in a:
        sum +=b.get(item)
    if sum <= 80:
        return 'kill me now'
    elif sum > 80 and sum <100:
        return 'i can handle this'
    elif sum >= 100:
        return 'party time!!'
