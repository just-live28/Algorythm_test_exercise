n, s = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
def func(k, total):
    global result
    if k == n:
        if total == s:
            result += 1
        return
    
    func(k+1, total)
    func(k+1, total + arr[k])
    
func(0, 0)
if s == 0:
    result -= 1

print(result)