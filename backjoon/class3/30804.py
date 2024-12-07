n = int(input())
fruits = list(map(int, input().split()))

left = right = 0
max_length = 0
fruit_types = set()
fruit_count = [0] * (max(fruits) + 1)

while right < n:
    fruit_types.add(fruits[right])
    fruit_count[fruits[right]] += 1
    
    while len(fruit_types) > 2:
        fruit_count[fruits[left]] -= 1
        if fruit_count[fruits[left]] == 0:
            fruit_types.remove(fruits[left])
        left += 1
    
    max_length = max(max_length, right - left + 1)
    right += 1

print(max_length)