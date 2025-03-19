m, n = map(int, input().split())

numbers = [True] * 1000001
numbers[0] = numbers[1] = False

for i in range(2, 1001):
    if not numbers[i]:
        continue
    j = i * i
    while j <= 1000000:
        numbers[j] = False
        j += i

for i in range(m, n+1):
    if numbers[i] == True:
        print(i)