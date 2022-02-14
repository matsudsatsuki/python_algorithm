from itertools import cycle
from heapq import heappush,heappop
inf = float('inf')

def idijkstra(G,s):
    Q,S = [(0,s)],set()
    while Q:
        d,u = heappop(Q)
        if u in S:
            continue
        S.add(u)
        yield u,d
        for v in G[u]:
            heappush(Q,(d+G[u][v],v))

def bidir_dijkstra(G,s,t):
    Ds,Dt = {},{}
    forw,back = idijkstra(G,s),idijkstra(G,t)
    dirs = (Ds,Dt,forw),(Dt,Ds,back)
    try:
        for D,other,step in cycle(dirs):
            v,d = next(step)
            D[v] = d
            if v in other:
                break
    except StopIteration:
        return inf
    m = inf
    for u in Ds:
        for v in G[u]:
            if not v in Dt:
                continue
            m = min(m,Ds[u]+G[u][v]+Dt[v])
    return m