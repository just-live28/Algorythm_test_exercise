word = input()
bomb = input()

stack = []
for s in word:
    stack.append(s)
    
    if len(stack) >= len(bomb):
        target = ''.join(reversed(stack[-1:-1-len(bomb):-1]))
        if target == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))