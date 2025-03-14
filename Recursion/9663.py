# func(k) : k개 퀸이 배치되어 있고, index k에 퀸을 배치해야 함
# k == n 이라면 count를 올리고 종료
# 세로 / 대각선 왼쪽 / 대각선 오른쪽

# 세 isused가 False인 경우 해당 위치에 놓고 세 isused True 처리 후 func(k+1) 실행, 이후 세 isused False 처리
# 대각선 왼쪽 : a + b 가 동일
# 대각선 오른쪽 : n + (a - b) 가 동일 (음수를 0으로 처리)

n = int(input())
isused1 = [False] * n
isused2 = [False] * (2 * n)
isused3 = [False] * (2 * n)

def func(k):
    global count
    if k == n:
        count += 1
        return
        
    for i in range(n):
        if not isused1[i] and not isused2[i + k] and not isused3[n + (i - k)]:
            isused1[i] = True
            isused2[i+k] = True
            isused3[n+(i-k)] = True
            func(k+1)
            isused1[i] = False
            isused2[i+k] = False
            isused3[n+(i-k)] = False
            
count = 0
func(0)
print(count)