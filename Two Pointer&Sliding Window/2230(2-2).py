# (2) 투 포인터 방식으로 풀기
# 두 수가 모두 자기 자신이 될 수 있음(N=1일때)
# 최대 차이는 20억이므로, 20억 + 1을 INF로 설정
INF = int(2e9) + 1
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

if n == 1:
    print(0)
elif n == 2:
    if arr[1] - arr[0] >= m:
        print(arr[1] - arr[0])
    else:
        print(0)
else:
    arr.append(2 * INF)
    min_result = INF
    en = 0
    for st in range(n):
        while arr[en] - arr[st] < m:
            en += 1
        min_result = min(min_result, arr[en] - arr[st])

    print(min_result)