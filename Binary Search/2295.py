# i j k 합-> l
# [두 개의 합] 안에 l - k 가 있는지 이분 탐색
from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
two = sorted([sum(x) for x in combinations_with_replacement(arr, 2)])

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

max_k = 0
for i in range(n):
    for j in range(n):
        k = arr[i] - arr[j]
        if i - j > 0 and binary_search(two, k, 0, len(two)-1) == 1:
            max_k = max(max_k, arr[i])

print(max_k)