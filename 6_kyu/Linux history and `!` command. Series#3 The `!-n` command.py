def bang_minus_n(n,history):
    length = len(history.split('\n'))
    history1 = history.split('\n')
    index = length-n
    for k in history1:
        if str(index+1) in k:
            return list(x for x in k.split('  ') if x !='')[1]
    else:
        return "!-%s: event not found" % n
