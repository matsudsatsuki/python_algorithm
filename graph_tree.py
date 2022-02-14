#二分木クラス
from turtle import left, right


class Tree:
    def __init__(self,left,right):
        self.left = left
        self.right = right

#多分木クラス
class Tree:
    def __init__(self,kids,next=None):
        self.kids = self.val = kids
        self.next = next

#Bunchパターン
class Bunch(dict):
    def __init__(self,*args,**kwds):
        super(Bunch,self).__init__(*args,**kwds)
        self.__dict__ = self

T = Bunch
t = T(left=T(left='a',right='b'),right=T(left='c'))
print(t.left)