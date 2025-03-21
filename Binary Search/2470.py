# 현재 값 -55
# 음수에서 0에 가까워지려면 left +
# 양수에서 0에 가까워지려면 right -

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = n-1
min_differ = abs(arr[left] + arr[right])
sol1, sol2 = arr[left], arr[right]
while left < right:    
    differ = arr[left] + arr[right]
    if differ == 0:
        sol1, sol2 = arr[left], arr[right]
        break
    elif abs(differ) < min_differ:
        min_differ = abs(differ)
        sol1, sol2 = arr[left], arr[right]
    
    if differ < 0:
        left += 1
    else:
        right -= 1

print(sol1, sol2)