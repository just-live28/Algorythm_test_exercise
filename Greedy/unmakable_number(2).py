n = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

# 1(init) -> 2 -> 3 -> 5 -> 8
# 이 숫자 이하의 값은 전부 만들 수 있다는 뜻.

target = 1
for num in numbers:
    if target < num:
        break
    target += num

print(target)
        

