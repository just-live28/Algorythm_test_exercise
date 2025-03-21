# 여는 기호 -> 스택에 추가

# 닫는 기호 -> 스택이 비어있으면 return 0 / 스택 최상단과 짝이 안맞으면 return 0
# 직전 문자가 같은 종류의 여는 기호였으면 total += score * (2 or 3) 이후 stack pop, score //= 2 or 3
# 아니면 그냥 stack pop, score //= 2 or 3

# 순회 후 스택이 남아있으면 return 0
def cal_total(string):
    total = 0
    score = 1
    stack = []
    prev = None
    for s in string:
        if s == '(':
            stack.append('(')
            score *= 2
        elif s == '[':
            stack.append('[')
            score *= 3
        else:
            if not stack or (s == ')' and stack[-1] == '[') or (s == ']' and stack[-1] == '('):
                return 0
            elif s == ')':
                if prev == '(':
                    total += score
                stack.pop()
                score //= 2
            elif s == ']':
                if prev == '[':
                    total += score
                stack.pop()
                score //= 3
        prev = s

    if stack:
        return 0
    else:
        return total

string = input()
print(cal_total(string))