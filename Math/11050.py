# from itertools import combinations

# n, k = map(int, input().split())
# arr = [x for x in range(1, n+1)]
# print(len(list(combinations(arr, k))))



def nck(n, k):
    result = 1
    a, b, c = 1, 1, 1
    while a <= n:
        result *= a
        a += 1
    while b <= n-k:
        result //= b
        b += 1
    while c <= k:
        result //= c
        c += 1
    return result

n, k = map(int, input().split())
print(nck(n, k))