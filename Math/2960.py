# N 작거나 같은 모든 소수를 찾기 위한 수 / K 번째 지워지는 숫자 출력

def eratos(n, k):
    visited = [False] * (n+1)
    visited[1] = True
    
    count = 0
    num = 2
    while num <= n:
        if not visited[num]:
            visited[num] = True
            count += 1
            
            if count == k:
                return num
            
            cur = num * num
            while cur <= n:
                if not visited[cur]:
                    visited[cur] = True
                    count += 1
                    
                    if count == k:
                        return cur
                    
                cur += num
            
        num += 1

n, k = map(int, input().split())

result = eratos(n, k)
print(result)