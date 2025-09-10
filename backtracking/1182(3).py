def func(k, total):
    global count
    if k == n:
        if total == s:
            count += 1
        return
    
    func(k+1, total)
    func(k+1, total + arr[k])

n, s = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

func(0, 0)

if s == 0:
    count -= 1
print(count)