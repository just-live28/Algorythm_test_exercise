import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    arr_a.sort()
    arr_b.sort()

    result = 0
    ptr_b = 0
    for a in arr_a:
        if ptr_b == m:
            result += m
            continue
        
        while a > arr_b[ptr_b]:
            ptr_b += 1
            if ptr_b == m:
                break
        result += ptr_b

    print(result)