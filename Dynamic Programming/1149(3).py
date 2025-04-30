# 1~N번 집
# 빨, 초, 파 중 하나로 칠해야 함 -> 각 집마다 해당 색으로 칠하는 비용 존재
# 규칙: 연속해서 같은 색이 나오지 않아야 함.

# d[i][color]: i번 집에 대해 color 색으로 칠했을 때 까지의 최소 비용 합
# d[i][0] = arr[i][0] + min(d[i-1][1], d[i-1][2])
# 초깃값
# d[1][0], d[1][1], d[1][2] = arr[1][0], arr[1][1], arr[1][2]
INF = int(1e9)

n = int(input())
arr = [None]
for _ in range(n):
    arr.append(list(map(int, input().split())))

d = [[INF] * 3 for _ in range(n+1)]
d[1][0], d[1][1], d[1][2] = arr[1][0], arr[1][1], arr[1][2]

for i in range(2, n+1):
    d[i][0] = arr[i][0] + min(d[i-1][1], d[i-1][2])
    d[i][1] = arr[i][1] + min(d[i-1][0], d[i-1][2])
    d[i][2] = arr[i][2] + min(d[i-1][0], d[i-1][1])

print(min(d[n]))