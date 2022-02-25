#一般的な分割統治法の実装
def divide_and_conquer(S,divide,combine):
    if len(S) == 1:
        return S
    L,R = divide(S)
    A = divide_and_conquer(L,divide,combine)
    B = divide_and_conquer(R,divide,combine)
    return combine(A,B)

