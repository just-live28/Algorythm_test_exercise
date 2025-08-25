# 뒤에서부터 순회하면서, 앞의 값이 더 크다면 맥스값을 교체, 이후 맥스값 - 현재값을 result에 추가
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = 0
    max_val = arr[n-1]
    for i in range(n-2, -1, -1):
        cur_val = arr[i]
        
        max_val = max(max_val, cur_val)
        result += max_val - cur_val
    
    print(result)