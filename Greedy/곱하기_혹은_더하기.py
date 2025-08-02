numbers = [int(x) for x in input()]

result = 0
for num in numbers:
    if result > 1:
        if num > 1:
            result *= num
        else:
            result += num
    else:
        result += num

print(result)