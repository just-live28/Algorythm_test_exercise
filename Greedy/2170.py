import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort()

st, en = arr[0]
result = 0
for i in range(1, n):
    x, y = arr[i]
    
    if x <= en and y >= en:
        en = y
    elif x > en:
        result += en - st
        st, en = x, y

result += en - st
print(result)