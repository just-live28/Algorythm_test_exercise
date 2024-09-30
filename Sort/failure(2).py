n = 4

stages = [4,4,4,4,4]

failures = []

for i in range(1, n+1):
    overs = len([x for x in stages if x > i])
    challenges = len([x for x in stages if x >= i])               
    
    if challenges == 0:
        failure = 0
    else:
        failure =  (challenges - overs) / challenges
    failures.append((i, failure))

failures.sort(key = lambda x : (-x[1], x[0]))
print(failures)

result = []
for i in failures:
    result.append(i[0])

print(result)