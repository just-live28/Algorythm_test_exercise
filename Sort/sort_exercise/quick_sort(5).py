array = [7,5,9,0,3,1,6,2,4,8]
n = len(array)

# def simple_quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[0]
#     tail = arr[1:]
    
#     left_side = [x for x in tail if x <= pivot]
#     right_side = [x for x in tail if x > pivot]
    
#     return simple_quick_sort(left_side) + [pivot] + simple_quick_sort(right_side)

# print(simple_quick_sort(array))

def quick_sort(arr, st, en):
    if st >= en:
        return
    
    pivot = st
    left = st + 1
    right = en
    while left <= right:
        while left <= en and arr[left] <= arr[pivot]:
            left += 1
        while right > st and arr[right] > arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, st, right - 1)
    quick_sort(arr, right + 1, en)

quick_sort(array, 0, n-1)
print(array)