n = 5
arr = [5,4,3,2,1]

def selection_sort(arr):
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
    return arr

print(selection_sort(arr))