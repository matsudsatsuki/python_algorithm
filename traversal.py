#隣接セットを使って表現したグラフの連結成分上の走査
def walk(G,s,S=set()):
    P,Q = dict(),set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v] = u
    return P

#連結成分の探索
def components(G):
    comp = []
    seen = set()
    for u in G:
        if u in seen:continue
        C = walk(G,u)
        seen.update(C)
        comp.append(C)
    return comp
