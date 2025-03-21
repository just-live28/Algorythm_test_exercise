# 여는 문자는 스택에 넣는다
# 닫는 문자면 스택이 있으면 pop, 스택이 비어 있으면 False
# 순회가 끝나고 스택이 남아 있으면 False

def is_vps(word):
    stack = []
    for i in word:
        if i == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True

n = int(input())
for _ in range(n):
    if is_vps(input()):
        print('YES')
    else:
        print('NO')