# 패러매트릭 서치, 최댓값

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

def split_trees(arr, target_height):
    result = 0
    for i in range(n):
        if arr[i] > target_height:
            result += arr[i] - target_height
    return result

start = 0
end = trees[-1]
max_height = 0
while start <= end:
    mid = (start + end) // 2
    
    current_m = split_trees(trees, mid)
    if current_m >= m:
        max_height = mid
        start = mid + 1
    else:
        end = mid - 1

print(max_height)