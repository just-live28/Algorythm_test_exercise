### 백트래킹으로 풀기 ###
# def func(n, total):
#     global count
#     if total >= n:
#         if total == n:
#             count += 1
#         return
    
#     for i in range(1, 4):
#         func(n, total + i)

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     count = 0
#     func(n, 0)
#     print(count)

### DP로 풀기 ###
## 테이블 d[k] : 정수 k를 1,2,3의 합으로 나타내는 방법의 수
## 점화식 찾기
# 1 - 1
# 2 - (1,1), (2)
# 3 - (1, 2), (1, 1, 1), (2, 1), (3)
# k가 4이상일 때,
# d[k] = d[k-3] + d[k-2] + d[k-1]

d = [0] * 11
d[1], d[2], d[3] = 1, 2, 4
for i in range(4, 11):
    d[i] = d[i-3] + d[i-2] + d[i-1]
t = int(input())
for _ in range(t):
    print(d[int(input())])