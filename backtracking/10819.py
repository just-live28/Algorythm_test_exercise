# n개의 정수 배열 A
# 0,1 차 절댓값, 1,2 차 절댓값 + 2,3 차 절댓값 ... + n-2, n-1 차 절댓값

# 수가 n개가 되었을 때 위의 값을 구한 뒤 최댓값인지 판단
# k 가 n-1일 때 수를 넣은 뒤 최종 판단 후 return

n = int(input())
arr = list(map(int, input().split()))

visited = [False] * n
def func(k, prev, result):
    global max_result
    if k == n:
        max_result = max(max_result, result)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result += abs(prev - arr[i])
            func(k+1, arr[i], result)
            visited[i] = False
            result -= abs(prev - arr[i])

max_result = 0
for i in range(n):
    visited[i] = True
    func(1, arr[i], 0)
    visited[i] = False

print(max_result)