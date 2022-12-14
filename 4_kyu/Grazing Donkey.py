https://www.codewars.com/kata/5b5ce2176d0db7331f0000c0

from math import acos, pi, sqrt

def area(r, R):
    return (
        r**2 * acos(r / 2 / R)
        + R**2 * acos(1 - r*r/2/R/R)
        - sqrt(r*r*(R+R-r)*(R+R+r)) / 2
    )

def get_rope_length(diameter, ratio):
    if ratio == 1:
        return diameter
    elif ratio * diameter == 0:
        return 0
    R = diameter / 2
    wanted = pi*R*R*ratio
    lo, hi = 0, diameter + 1
    while lo < hi - 1:
        m = (lo + hi) // 2
        a = area(m, R)
        if a < wanted:
            lo = m
        else:
            hi = m
    return lo