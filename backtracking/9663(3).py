# k개의 퀸을 정한 상태. k번째 퀸을 배치하는 함수.
def func(k):
    global count
    if k == n:
        count += 1
        return
    
    for i in range(n):
        if not visited1[i] and not visited2[k+i] and not visited3[k-i+15]:
            visited1[i] = True
            visited2[k+i] = True
            visited3[k-i+15] = True
            func(k+1)
            visited1[i] = False
            visited2[k+i] = False
            visited3[k-i+15] = False
        

n = int(input())
visited1 = [False] * n      # 세로
visited2 = [False] * 50     # 왼쪽 아래 방향 대각선
visited3 = [False] * 50     # 오른쪽 아래 방향 대각선
count = 0

func(0)
print(count)