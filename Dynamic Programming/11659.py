# 테이블
# d[i] : 처음부터 i번째 수까지의 총합
# 점화식
# d[i] = d[i-1] + arr[i]
# 초기값 x
# 구하는 값: a, b를 받았을 때 d[b] - d[a-1]
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
d = [0] * (n+1)

for i in range(1, n+1):
    d[i] = d[i-1] + arr[i]
for _ in range(m):
    a, b = map(int, input().split())
    print(d[b] - d[a-1])