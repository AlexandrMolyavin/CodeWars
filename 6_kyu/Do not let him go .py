from typing import List, Tuple


def locate_entrance(office: List[str]) -> Tuple[int, int]:
    r = 1
    c = office[0].index('#')+1
    if office[r][c] == '#':
        c+=1
    queue =[[r,c]]
    visited = []
    m = 0
    for i in office:
        m = max(m,len(i))
    for i in range(0,len(office)):
        visited.append([False]*m)
    for i in range(0,len(office)):
        office[i]+= " "*(m-len(office[i]))
    visited[r][c] = True
    while len(queue)!=0:
        q = queue.pop()
        r = q[0]
        c = q[1]
        visited[r][c] = True
        if r==0 or c==0:
            return (c,r)
        if r==len(office)-1 or c ==len(office[r])-1:
            return (c,r)
        if r>0:
            if office[r-1][c] ==' ':
                return (c,r)
            if not visited[r-1][c] and office[r-1][c] == '.':
                queue.append([r-1,c])
        if c>0:
            if office[r][c-1] ==' ':
                return (c,r)
            if not visited[r][c-1] and office[r][c-1] == '.':
                queue.append([r,c-1])
        if r < len(office)-1:
            if office[r+1][c] ==' ':
                return (c,r)
            if not visited[r+1][c] and office[r+1][c] == '.':
                queue.append([r+1,c])
        if c<len(office[r])-1:
            if office[r][c+1] ==' ':
                return (c,r)
            if not visited[r][c+1] and office[r][c+1] == '.':
                queue.append([r,c+1])