word = input()

stk = []
result = ''
is_tag = False
for i in range(len(word)):
    if word[i] == '<':
        while stk:
            result += stk.pop()
        is_tag = True
        result += '<'
        continue
    elif word[i] == '>':
        is_tag = False
        result += '>'
        continue
    
    if is_tag:
        result += word[i]
        continue
    
    if word[i] == ' ':
        while stk:
            result += stk.pop()
        result += ' '
    else:
        stk.append(word[i])

while stk:
    result += stk.pop()

print(result)