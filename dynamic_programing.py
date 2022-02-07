from functools import cache, wraps
import re

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