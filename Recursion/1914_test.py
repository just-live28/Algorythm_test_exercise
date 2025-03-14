import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 설정

def hanoi(n, start, sub, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, end, sub)
    print(start, end)
    hanoi(n - 1, sub, start, end)

n = int(input())

# n >= 20일 때는 O(1) 연산만 수행하여 빠르게 처리
if n > 20:
    print(2**n - 1)
else:
    print(2**n - 1)
    hanoi(n, 1, 2, 3)