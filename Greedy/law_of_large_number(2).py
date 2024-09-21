# n개의 자연수 / m번 더하기 / 같은 숫자 k번 연속 초과 불가 

# 한 사이클
# 제일 큰수 k 번
# 두번째로 큰 수 1 번

# m이 9이고 k가 3일때
# 6과 5
# (m // (k+1))(k * first + second) + (m % (k+1)) * first
# 2사이클 + 제일큰수 1번

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

first, second = numbers[0], numbers[1]

result = (m // (k+1)) * (k * first + second) + (m % (k+1)) * first
print(result)
