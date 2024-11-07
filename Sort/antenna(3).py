n = int(input())

index = n // 2
if n % 2 == 0:
    index -= 1

houses = list(map(int, input().split()))
houses.sort()

print(houses[index])