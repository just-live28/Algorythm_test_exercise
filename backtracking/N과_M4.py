# 중복 허용(visited 미사용) / 비내림차순(적어도 작으면 안됨) -> 중복 조합

def func(k):
    if k == m:
        print(*result)
        return
    
    if k == 0:
        st = 1
    else:
        st = result[k-1]
    
    for i in range(st, n+1):
        result[k] = i
        func(k+1)
        
n, m = map(int, input().split())
result = [0] * m
func(0)