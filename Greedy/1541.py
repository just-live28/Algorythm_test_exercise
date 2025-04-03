word = input().split('-')

if word[0].isdigit():
    result = int(word[0])
else:
    result = sum([int(x) for x in word[0].split('+')])

for i in range(1, len(word)):
    # word[i]
    if word[i].isdigit():
        result -= int(word[i])
    else:
        result -= sum([int(x) for x in word[i].split('+')])
    
print(result)