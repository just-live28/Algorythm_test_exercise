N = 4
stages = [4,4,4,4,4]

history = [0] * (N+2)
for stage in stages:
    history[stage] += 1

reverse_history = history[::-1]
clears = [0] * (N+1)
prev = 0
for i in range(len(reverse_history)):
    prev += reverse_history[i]
    clears[-i] = prev

failures = []
for i in range(1, N + 1):
    if clears[i] == 0:
        failures.append((i, 0))
    else:
        failures.append((i,history[i] / clears[i]))

print([x[0] for x in sorted(failures, key = lambda x : (-x[1], x[0]))])