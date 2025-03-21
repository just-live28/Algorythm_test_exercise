# 정확히 그 값과 일치하면 그 인덱스를 가리키기 때문에 그 인덱스를 반환
# 중간 값에 대해서 오른쪽 인덱스를 가리키게됨.
# 그렇다면 중간 값일 때 i와 i-1의 값을 각각 비교해 더 가까운 쪽(인덱스)을 반환

from bisect import bisect_left

# m 사대 n 동물 l 사거리
m, n, l = map(int, input().split())
fires = list(map(int, input().split()))
fires.sort()

def find_near_hunter(arr, x):
    idx = bisect_left(arr, x)
    if idx == 0:
        return 0
    elif idx == m:
        return m-1    
    elif arr[idx] == x:
        return idx
    else:  
        if abs(arr[idx] - x) < abs(arr[idx-1] - x):
            return idx
        else:
            return idx-1

def is_dead(x, y):
    if y > l:
        return False
    
    hunter_x = fires[find_near_hunter(fires, x)]
    if abs(hunter_x - x) + y <= l:
        return True
    return False

count = 0
for _ in range(n):
    a, b = map(int, input().split())
    if is_dead(a, b):
        count += 1
print(count)