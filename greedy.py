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
