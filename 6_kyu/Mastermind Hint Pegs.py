def get_hints(a, guess):
    answer = list(x for x in a)
    wh = 0
    bl = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            bl += 1
            guess[i] = 'g'
            answer[i] = 'a'

    for i in range(len(guess)):
        if guess[i] in answer:
            j = answer.index(guess[i])
            wh += 1
            answer[j] = 'a'
            guess[i] = 'g'

    return {"black": bl, "white": wh}