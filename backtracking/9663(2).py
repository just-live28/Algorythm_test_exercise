n = int(input())

# 행
isused1 = [False] * 15
# 왼쪽 아래 대각선
isused2 = [False] * 30
# 오른쪽 아래 대각선
isused3 = [False] * 30

count = 0
def queen(k):
    global count
    if k == n:
        count += 1
        return
    
    for i in range(n):
        if not isused1[i] and not isused2[k+i] and not isused3[k-i+n-1]:
            isused1[i] = True
            isused2[k+i] = True
            isused3[k-i+n-1] = True
            queen(k+1)
            isused1[i] = False
            isused2[k+i] = False
            isused3[k-i+n-1] = False

queen(0)
print(count)