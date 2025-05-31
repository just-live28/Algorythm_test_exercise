n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.append(0)

max_area = 0
stk = []
for i in range(n+1):
    left = i
    while stk and stk[-1][0] > arr[i]:
        top_h, top_idx = stk.pop()
        max_area = max(max_area, top_h * (i - top_idx))
        left = top_idx
    stk.append((arr[i], left))

print(max_area)