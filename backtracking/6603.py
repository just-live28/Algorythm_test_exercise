# 1~49 중 6개 수 고르기
# k(k>6)개의 수를 골라 집합을 만든 후 그 수에서 번호 선택
# func(n) : n개의 수가 골라진 상태. idx n번째 수를 고르는 함수
def func(n):
    global result
    if n == 6:
        print(*arr[:-1])
        return 

    for i in range(k):
        if not visited[i] and numbers[i] > arr[n-1]:
            visited[i] = True
            arr[n] = numbers[i]
            func(n+1)
            visited[i] = False
            
while True:
    line = list(map(int, input().split()))
    if len(line) == 1 and line[0] == 0:
        break
    
    k = line[0]
    numbers = line[1:]
    arr = [0] * 7
    visited = [False] * k
    func(0)
    print()