from bisect import bisect_left, bisect_right

def cal_num(arr, left_value, right_value):
    return bisect_right(arr, right_value) - bisect_left(arr, left_value)

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
finds = list(map(int, input().split()))
for i in range(m):
    print(cal_num(arr, finds[i], finds[i]), end=' ')