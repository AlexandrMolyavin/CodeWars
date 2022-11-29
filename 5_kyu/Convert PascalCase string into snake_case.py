def to_underscore(string):
    string = str(string)
    res = ""
    j = 0
    for i in range(len(string)-1):
        if string[i+1].isupper():
            res += string[j:i+1].lower() + "_"
            j = i+1
    res += string[j:].lower()
    return res