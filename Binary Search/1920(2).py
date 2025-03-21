# 자연수 N (1~10만)
# n개의 수열
# 자연수 M (1~10만)
# m개의 수들이 n개의 수열 안에 존재하는지 여부 반환 : 1 존재 0 비존재

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
finds = list(map(int, input().split()))
for target in finds:
    print(binary_search(arr, target, 0, n-1))