#隣接セットを使って表現したグラフの連結成分上の走査
from tkinter.messagebox import NO


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

#再帰的木の巡回
def tree_walk(T,r):
    for u in T[r]:
        tree_walk(T,u)

#再帰を使った深さ優先探索
def rec_dfs(G,s,S=None):
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        rec_dfs(G,u,S)
    return S

#反復を使った深さ優先探索
def iter_dfs(G,s):
    S,Q = set(),[]
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:continue
        S.add(u)
        Q.extend(G[u])
        yield u

#グラフの一般的な巡回関数
def traverse(G,s,qtype=set):
    S,Q = set(),qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S:continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u

#タイムスタンプ付き深さ優先探索
def dfs(G,s,d,f,S=None,t=0):
    if S is None:S=set()
    d[s] = t;t+=1
    S.add(s)
    for u in G[s]:
        if u in S:continue
        t = dfs(G,u,d,f,S,t)
    f[s] = t; t+=1
    return t