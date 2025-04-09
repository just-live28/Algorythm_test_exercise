def fib(n, memo):
    if n <= 1:
        return n
    
    if n not in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

memo = {}
n = 5
print(fib(n, memo))     # 출력: 5