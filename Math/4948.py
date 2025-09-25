# 2n 까지의 소수를 에라토스 체로 구하기
# n < x <= 2n 사이의 소수 개수 세기
visited = [True] * (123456 * 2 + 1)

num = 2
while num * num <= 123456 * 2:
    if not visited[num]:
        num += 1
        continue
    
    cur = num * num
    while cur <= 123456 * 2:
        visited[cur] = False
        cur += num
    
    num += 1

while True:
    n = int(input())
    if n == 0:
        break
    
    result = 0
    for i in range(n+1, 2*n+1):
        if visited[i]:
            result += 1

    print(result)