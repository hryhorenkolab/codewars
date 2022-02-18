def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for i in arr:
        if i>0:
            pos += 1
        else:
            neg += i
    return [pos, neg]
