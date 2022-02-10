from collections import defaultdict
from itertools import chain



def tr(G):
    GT = {}
    for u in G:
        GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT

def match(G,X,Y):
    H = tr(G)
    S,T,M = set(X),set(Y),set()
    while S:
        s = S.pop()
        Q,P ={s},{}
        while Q:
            u = q.pop()
            if u in T:
                T.remove(u)
                break
            forw = (v for v in G[u] if (u,v) not in M)
            back = (v for v in H[u] if (v,u) not in M)
            for v in chain(forw,back):
                if v in P:
                    P[v] = u
                    Q.add(v)
            while u != s:
                u,v = P[u],u
                if v in G[u]:
                    M.add((u,v))
                else:
                    M.remove((v,u))
    return M