#隣接セットを使って表現したグラフの連結成分上の走査
from collections import deque
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

#深さ優先探索に基づいたトポロジカルソート
def dfs_topsort(G):
    S,res = set(),[]
    def recurse(u):
        if u in S:
            return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)
    for u in G:
        recurse(u)
    res.reverse()
    return res

#反復深化深さ優先探索（IDDFS）
def iddfs(G,s):
    yielded = set()
    def recurse(G,s,d,S=None):
        if s not in yielded:
            yield s
            yielded.add(s)
        if d == 0:
            return
        if S is None:
            S = set()
        S.add(s)
        for u in G[s]:
            if u in S:
                continue
            for v in recurse(G,u,d-1,S):
                yield v
    n = len(G)
    for d in range(n):
        if len(yielded) == n:
            break
        for u in recurse(G,s,d):
            yield u
    
#幅優先探索
def bfs(G,s):
    P,Q = {s:None},deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P:
                continue
            P[v] = u
            Q.append(v)
    return P

#強連結成分を見つけるKosarajuのアルゴリズム
def tr(G):
    GT = {}
    for u in G:
        GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT

def scc(G):
    GT = tr(G)
    sccs,seen = [],set()
    for u in dfs_topsort(G):
        if u in seen:
            continue
        C = walk(GT,u,seen)
        seen.update(C)
        sccs.append(C)
    return sccs
