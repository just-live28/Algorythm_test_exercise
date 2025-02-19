# 테이블
# d[i] : 2 * i 크기 직사각형을 채우는 방법의 수
# 점화식
# d[i] = d[i-2] * 2 + d[i-1]
# 초기값
# d[1], d[2] = 1, 2

n = int(input())
d = [0] * (n+1)
d[1] = 1
if n >= 2:
    d[2] = 2
if n >= 3:
    for i in range(3, n+1):
        d[i] = (d[i-2] + d[i-1]) % 10007

print(d[n])