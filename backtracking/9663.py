n = int(input())

visited1 = [False] * 15
visited2 = [False] * 30
visited3 = [False] * 30

result = 0
def func(k):
    global result
    if k == n:
        result += 1
        return
    
    for i in range(n):
        if not visited1[i] and not visited2[i-k+n-1] and not visited3[k+i]:
            visited1[i] = True
            visited2[i-k+n-1] = True
            visited3[k+i] = True
            func(k+1)
            visited1[i] = False
            visited2[i-k+n-1] = False
            visited3[k+i] = False

func(0)
print(result)