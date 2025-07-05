n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0

count = 0
cur = 0
while True:
    if left == n and right == n:
        break
    elif right == n:
        if cur == m:
            count += 1
        while cur >= m:
            left += 1
            cur -= arr[left-1]
            if cur == m:
                count += 1
        break
    
    if cur < m:
        right += 1
        cur += arr[right-1]
    elif cur == m:
        count += 1
        left += 1
        cur -= arr[left-1]
    else:
        left += 1
        cur -= arr[left-1]

print(count)