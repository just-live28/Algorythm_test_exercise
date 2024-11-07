n = int(input())
parts = list(map(int, input().split()))
parts.sort()
m = int(input())
finds = list(map(int, input().split()))

def binary_search(array, start, end, target):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, mid+1, end, target)
    else:
        return binary_search(array, start, mid-1, target)

results = []
for f in finds:
    result = binary_search(parts, 0, n, f)
    
    if result == None:
        results.append('no')
    else:
        results.append('yes')

for result in results:
    print(result, end=' ')