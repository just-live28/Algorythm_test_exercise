from itertools import combinations_with_replacement

n = int(input())

arr = [2, 3, 5]
numbers = []
numbers.append(1)

i = 1
while(len(numbers) < 1000): 
    for nums in list(combinations_with_replacement(arr, i)):
        total = 1
        for num in nums:
            total *= num
        numbers.append(total)
        if len(numbers) >= 1000:
            break
    i += 1
result = sorted(numbers)

print(result[n-1])