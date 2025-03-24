def find_min_length(arr, left, right):
    if left == right:
        return float('inf')
    if right - left == 1:
        return (arr[left][0] - arr[right][0]) ** 2 + (arr[left][1] - arr[right][1]) ** 2
    mid = (left + right) // 2
    
    dist = min(find_min_length(arr, left, mid), find_min_length(arr, mid+1, right))
    mid_x = arr[mid][0]
    candidates = []
    for i in range(left, right + 1):
        if (arr[i][0] - mid_x) ** 2 <= dist:
            candidates.append(arr[i])
    candidates.sort(key=lambda x : x[1])
    
    min_d = dist
    for i in range(len(candidates)):
        for j in range(i+1, min(i + 7, len(candidates))):
            dx = candidates[j][0] - candidates[i][0]
            dy = candidates[j][1] - candidates[i][1]
            if dy ** 2 > dist:
                break
            min_d = min(min_d, dx ** 2 + dy ** 2)
    return min_d

n = int(input())
dots = set()
for _ in range(n):
    a, b = map(int, input().split())
    dots.add((a, b))
if len(dots) < n:
    print(0)
else:
    dots = sorted(list(dots), key=lambda x : (x[0]))
    print(find_min_length(dots, 0, n-1))