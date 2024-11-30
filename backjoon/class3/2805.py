import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))

min_height = 0
max_height = max(trees)

result = 0
while min_height <= max_height:
    mid = (min_height + max_height) // 2
    
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    
    if total >= m:
        result = mid
        min_height = mid + 1
    else:
        max_height = mid - 1

print(result)