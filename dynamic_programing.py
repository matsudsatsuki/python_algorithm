from functools import cache, wraps
import re

from sympy import topological_sort

def memo(func):
    cache = {}                        #部分問題の解をキャッシュする
    @wraps(func)                      #wrapはfuncのように見せる
    def wrap(*args):                  #メモ化するラッパー関数
        if args not in cache:         #既に計算されているかどうか
            cache[args] = func(*args) #されていない場合、計算し、その解をキャッシュ
        return cache[args]            #キャッシュされている解を返す
    return wrap                       #ラッパー関数を返す


@memo
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n = int(input())
print(fibo(n))

#メモ化を使った再帰的DAG最短経路
def rec_dag_sp(W,s,t):                         #sからtへの最短経路
    @memo                                      #dをメモ化
    def d(u):                                  #uからtまでの距離
        if u == t:                             #到着している場合
            return 0                                                                           
        return(min(W[u][v]+d(u) for v in W[u]))#今のステップから選べる最短経路の距離
    return d(s)                                #dを実際の始点ノードsに適用

#DAG最短経路
def dag_sp(W,s,t):                             #sからtまでの最短経路
    d = {u:float('inf')for u in W}             #距離の推定
    d[s] = 0                                   #始点ノード　
    for u in topological_sort(W):              #トポロジカルソートの順序で
        if u == t:                             #既に到着済みの場合　
            continue
        for v in W[u]:                         #各出力エッジに対して
            d[v] = min(d[v],d[u]+W[u][v])      #エッジを緩和
    return d[t]                                #(sから)tへの距離


#最長増加部分列問題に対するメモ化と再帰を使った解法
def rec_lis(seq):                            #最長増加部分列の長さを計算
    @memo                        
    def L(cur):                              #seq[cur]で終わる最長部分列
        res = 1                              #長さは少なくとも1
        for pre in range(cur):               #先行ノードの候補を走査していく
            if seq[pre] <= seq[cur]:         #有効な(小さい)先行ノードの場合
                res = max(res,1+L(pre))      #解を改善するか?
        return res
    return max(L(i) for i in range(len(seq)))#最長増加部分列の長さを返す
#