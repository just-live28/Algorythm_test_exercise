n = int(input())

# 열 y
visited1 = [False] * n
# 왼쪽아래 대각선 x+y
visited2 = [False] * 30 
# 오른쪽아래 대각선 x-y+n-1
visited3 = [False] * 30

def func(k):
    global result
    if k == n:
        result += 1
        return
    
    for i in range(n):
        if not visited1[i] and not visited2[k+i] and not visited3[k-i+n-1]:
            visited1[i] = True
            visited2[k+i] = True
            visited3[k-i+n-1] = True
            func(k+1)
            visited1[i] = False
            visited2[k+i] = False
            visited3[k-i+n-1] = False

result = 0
func(0)
print(result)