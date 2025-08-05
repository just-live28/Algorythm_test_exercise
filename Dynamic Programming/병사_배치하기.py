# n 명수 / arr 숫자 리스트
# LIS를 구하고, n에서 이 최대 명수를 빼기
n = int(input())
arr = list(map(int, input().split()))
arr.reverse()

d = [1] * (n+1)

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))