#再帰を使った挿入ソート
def ins_sort_rec(seq,i):
    if i == 0:
        return 
    ins_sort_rec(seq,i-1)
    j = 1
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1],seq[j] = seq[j],seq[j-1]
        j -= 1

#反復を使った挿入ソート
def ins_sort(seq):
    for i in range(1,len(seq)):
        j = 1
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1],seq[j] = seq[j],seq[j-1]
            j -= 1

#再帰を使った選択ソート
def sel_sort_rec(seq,i):
    if i == 0: return
    max_j = i
    for j in range(i):
        if seq[j] > seq[max_j]: max_j = j
    seq[i],seq[max_j] = seq[max_j],seq[i]
    sel_sort_rec(seq,i-1)

#反復を使った選択ソート
def sel_sort(seq):
    for i in range(len(seq-1),0,-1):
        max_j = i
        for j in range(i):
            if seq[j] > seq[max_j]:
                max_j = j
        seq[i],seq[max_j] = seq[max_j],seq[i]
        