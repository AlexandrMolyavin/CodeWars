def shoot(results):
    p1_score = 0
    p2_score = 0

    for item in results:
        if item[1]:
            inc = 2
        else:
            inc = 1

        p1_shoots = item[0]['P1']
        p2_shoots = item[0]['P2']

        for shoot in p1_shoots:
            if shoot == 'X':
                p1_score += inc

        for shoot in p2_shoots:
            if shoot == 'X':
                p2_score += inc

    if p1_score > p2_score:
        return 'Pete Wins!'
    elif p1_score < p2_score:
        return 'Phil Wins!'
    else:
        return 'Draw!'