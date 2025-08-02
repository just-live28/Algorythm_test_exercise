def is_correct(word):
    stack = []
    for w in word:
        if w == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            elif stack[-1] == '(':
                stack.pop()
            else:
                return False
    
    if stack:
        return False
    return True

def split_word(word):
    count = 0
    for i in range(len(word)):
        if word[i] == '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return i
    return len(word)
    
def solution(p):
    if p == '':
        return p
    
    idx = split_word(p)
    u = p[:idx+1]
    v = p[idx+1:]
    
    if is_correct(u):
        return u + solution(v)
    else:
        tmp = ''
        tmp += '('
        tmp += solution(v)
        tmp += ')'
        
        u = u[1:-1]
        for t in u:
            if t == '(':
                tmp += ')'
            else:
                tmp += '('
        
        return tmp