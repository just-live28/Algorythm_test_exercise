group = input().split('-')

result = sum(map(int, group[0].split('+')))


for each in group[1:]:
    result -= sum(map(int, each.split('+')))

print(result)