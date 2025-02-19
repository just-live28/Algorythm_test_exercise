# r g b 3색
# 이전 집과 색이 달라야 한다.

# 테이블
# d[k][0|1|2] : k번째 집을 각각 R, G, B로 칠했을 경우 총 비용 합의 최솟값.

# 점화식
# d[k][0] = min(d[k-1][2], d[k-1][1]) + h[k][0]
# d[k][1] = min(d[k-1][0], d[k-1][2]) + h[k][1]
# d[k][2] = min(d[k-1][0], d[k-1][1]) + h[k][2]

# 초기값
# d[1] = h[1]

n = int(input())
d = [[0,0,0] for _ in range(n+1)]
h = [[None]]
for _ in range(n):
    h.append(list(map(int, input().split())))

d[1] = h[1]
for k in range(2, n+1):
    d[k][0] = min(d[k-1][2], d[k-1][1]) + h[k][0]
    d[k][1] = min(d[k-1][0], d[k-1][2]) + h[k][1]
    d[k][2] = min(d[k-1][0], d[k-1][1]) + h[k][2]

print(min(d[n]))