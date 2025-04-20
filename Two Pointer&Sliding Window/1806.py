# 포인터 left, right
# 부분합이 S미만이면 right 증가
# S이상이면 min_length 갱신 후 left 증가

# 부분합이 S이상인 부분수열 중 가장 짧은 것(min_length)

n, s = map(int, input().split())
arr = list(map(int, input().split()))

min_length = 100001
left = 0
right = 0
each_sum = arr[0]
while True:
    if left == n or right == n:
        break
    
    if each_sum >= s:
        min_length = min(min_length, right-left+1)
        each_sum -= arr[left]
        left += 1
    else:
        right += 1
        if right < n:
            each_sum += arr[right]

if min_length == 100001:
    print(0)
else:
    print(min_length)