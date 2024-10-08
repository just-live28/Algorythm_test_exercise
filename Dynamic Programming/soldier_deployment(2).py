# d[i] : array[i] 를 마지막 원소로 가지는 '증가하는 부분 수열'의 최대 길이
# 이 문제는 내림차순이므로, 이 최대길이를 전체 명수에서 뺀 것이 정답

n = int(input())

array = list(map(int, input().split()))
array.reverse()

d = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + 1)

print(n-max(d))