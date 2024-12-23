n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

first = arr[0]
second = arr[1]

result = (first * k + second) * (m // (k+1)) + first * (m % (k+1))
print(result)