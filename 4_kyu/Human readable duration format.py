https://www.codewars.com/kata/52742f58faf5485cae000b9a


def format_duration(seconds):
    if seconds == 0: return "now"

    durationStr = ['year', 'day', 'hour', 'minute', 'second']
    dur = [0] * 5

    dur[3], dur[4] = divmod(seconds, 60)
    dur[2], dur[3] = divmod(dur[3], 60)
    dur[1], dur[2] = divmod(dur[2], 24)
    dur[0], dur[1] = divmod(dur[1], 365)

    lastNonZero = [i for i in range(len(dur)) if dur[i] != 0][::-1][0]
    out = ''
    c = 0

    for i in range(0, 5):
        if dur[i] > 0:
            if i == lastNonZero and c > 0:
                out += ' and '
            elif c != 0:
                out += ', '
            out += str(dur[i]) + ' ' + durationStr[i]
            if dur[i] > 1: out += 's'
            c += 1

    return out