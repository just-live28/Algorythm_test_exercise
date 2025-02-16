n, s = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
def func(k, score):
    global result
    if k == n:
        if score == s:
            result += 1 
        return
    
    func(k+1, score + arr[k])
    func(k+1, score)

func(0, 0)
if s == 0:
    result -= 1
print(result)