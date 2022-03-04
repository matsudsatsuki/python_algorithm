from heapq import heapify,heappop,heappush
from inspect import trace
from itertools import count

#huffmanのアルゴリズム
def huffman(seq,frq):
    num = count()
    trees = list(zip(frq,num,seq))
    heapify(trees)
    while len(trees) > 1:
        fa,_,a = heappop(trees)
        fb,_,b = heappop(trees)
        n = next(num)
        heappush(trees,(fa+fb,n,[a,b]))
    return trees[0][-1]
    seq = 'abcdefghi'
    frq = [4,5,6,9,11,12,15,16]

#huffman木からhuffmanコードを抽出
def codes(tree,prefix=''):
    if len(tree) == 1:
        yield (tree,prefix)
        return
    for bit,child in zip('01',tree):
        for pair in codes(child,prefix+bit):
            yield pair
#Kruskalのアルゴリズムの簡単な実装
def naive_find(C,u):
    while C[u] != u:
        u = C[u]
    return u

def naive_union(C,u,v):
    u = naive_find(C,u)
    v = naive_find(C,v)
    C[u] = v

def naive_kruskal(G):
    E = [(G[u][v],u,v) for u in G for v in G[u]]
    T = set()
    C = {u:u for u in G }
    for _, u, v in sorted(E):
        if naive_find(C,u) != naive_find(C,v):
            T.add((u,v))
            naive_union((C,u,v))
    return T

#kruskalのアルゴリズム
def find(C,u):
    if C[u] != u:
        C[u] = find(C,C[u])#パス圧縮
    return C[u]

def union(C,R,u,v):
    u,v = find(C,u),find(C,v)
    if R[u] > R[v]:#ランクによる統合
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:
        R[v] += 1#同ランクの場合,vを一つ上にあげる

def kruskal(G):
    E = [(G[u][v],u,v)for u in G for v in G[u]]
    T = set()
    C,R = {u:u for u in G},{u:0 for u in G}#成分の代表とランク
    for _,u,v in sorted(E):
        if find(C,u) != find(C,v):
            T.add((u,v))
            union(C,R,u,v)
    return T

#Primのアルゴリズム
from heapq import heappop,heappush

def prim(G,s):
    P,Q = {},[(0,None,s)]
    while Q:
        _,p,u = heappop(Q)
        if u in P:
            continue
        P[u] = p
        for v,w in G[u].items():
            heappush(Q,(w,u,v))
    return P
    

