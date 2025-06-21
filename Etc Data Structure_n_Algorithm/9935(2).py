word = input()
bomb = input()
n = len(bomb)

stk = []
for i in word:
    stk.append(i)

    if len(stk) >= n and ''.join(stk[-n:]) == bomb:
        for _ in range(n):
            stk.pop()

if stk:
    print(''.join(stk))
else:
    print('FRULA')