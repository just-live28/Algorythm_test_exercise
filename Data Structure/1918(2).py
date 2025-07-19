exp = input()

def infix_to_postfix(exp):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    result = []

    for token in exp:
        if token.isalpha():
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and prec.get(token, 0) <= prec.get(stack[-1], 0):
                result.append(stack.pop())
            stack.append(token)
    
    while stack:
        result.append(stack.pop())

    return ''.join(result)

print(infix_to_postfix(exp))