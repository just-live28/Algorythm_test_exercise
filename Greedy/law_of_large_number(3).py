# n 배열 크기 / m 더하는 횟수 / k 동일 수 덧셈 가능 횟수

n, m, k = map(int, input().split())

# 1사이클 : (fir * k + sec) * (m // (k+1))
# 나머지는 fir * (m % (k+1))

array = list(map(int, input().split()))
array.sort(reverse=True)

first, second = array[0], array[1]

result = (first * k + second) * (m // (k+1)) + first * (m % (k+1))

print(result)