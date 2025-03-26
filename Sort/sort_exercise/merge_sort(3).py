def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = [0] * (len(left) + len(right))
    pl, pr = 0, 0
    for i in range(len(result)):
        if pl == len(left):
            result[i] = right[pr]
            pr += 1
        elif pr == len(right):
            result[i] = left[pl]
            pl += 1
        else:
            if left[pl] <= right[pr]:
                result[i] = left[pl]
                pl += 1
            else:
                result[i] = right[pr]
                pr += 1
    return result
    
arr = [1,3,7,15,2,5]
print(*merge_sort(arr))