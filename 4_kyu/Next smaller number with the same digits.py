https://www.codewars.com/kata/5659c6d896bc135c4c00021e

def next_smaller(n):
    s=str(n)
    l=len(s)-2
    while l>=0 and s[l]<=s[l+1]:
        l -= 1
    if l>=0:
        upper = s[:l]
        lower = s[l:]
        lower_list=[c for c in lower]
        for i in range(len(lower_list)-1,0,-1):
            if  lower_list[0]>lower_list[i] and (lower_list[i] != '0' or len(upper)>0):
                x = lower_list[i]
                lower_list[i] = lower_list[0]
                lower_list[0] = x
                lower_list[1:]=sorted(lower_list[1:], reverse=True)
                return int(upper+"".join(lower_list))
    return -1