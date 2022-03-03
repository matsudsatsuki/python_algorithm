#一般的な分割統治法の実装
import re
from turtle import right


def divide_and_conquer(S,divide,combine):
    if len(S) == 1:
        return S
    L,R = divide(S)
    A = divide_and_conquer(L,divide,combine)
    B = divide_and_conquer(R,divide,combine)
    return combine(A,B)
#二分探索木の挿入と実装
class Node:
    left = None
    right = None
    def __init__(self,key,val):
        self.key = key
        self.val = val

def insert(node,key,val):
    if node is None:
        return Node(key,val)
    if node.key == key:
        node.val = val
    elif key < node.key:
        node.left = insert(node.left,key,val)
    else:
        node.right = insert(node.right,key,val)
    return node
def search(node,key):
    if node is None:
        raise KeyError
    if node.key == key:
        return node.val
    elif key < node.key:
        return search(node.left,key)
    else:
        return search(node.right,key)

class Tree:
    root = None
    def __setitem__(self,key,val):
        self.root = insert(self.root,key,val)
    def __getitem__(self,key):
        return search(self.root,key)
    def __contains__(self,key):
        try: search(self.root,key)
        except KeyError: return False
        return True

#分割アルゴリズムと選択アルゴリズムの直感的な実装
def partition(seq):
    pi,seq = seq[0],seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo,pi,hi

def select(seq,k):
    lo,pi,hi = partition(seq)
    m = len(lo)
    if m == k:
        return pi
    elif m < k:
        return select(hi,k-m-1)
    else:
        return select(lo,k)

def mergesort(seq):
    mid = len(seq)//2
    left,right = seq[:mid],seq[mid:]
    if len(left) > 1:
        left = mergesort(left)
    if len(right) > 1:
        right = mergesort(right)
    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res
    
