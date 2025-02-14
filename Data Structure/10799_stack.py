pipe = input()

q = []
count = 0
for s in pipe:
    if s == '(':
        q.append(1)
    elif s == ')':
        if q[-1] == 1:
            q.pop()
            for i in range(len(q)):
                q[i] += 1
        else:
            count += q.pop()

print(count)