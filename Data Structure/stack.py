stack = []
pos = -1

def push(n):
    global pos
    stack.append(n)
    pos += 1

def pop():
    global pos
    if pos == -1:
        print('빈 스택')
        return
    pos -= 1
    return stack.pop()

def top():
    if pos == -1:
        return None
    return stack[pos]

push(1)
push(2)
push(3)

pop()
pop()
pop()
pop()
print(top())

