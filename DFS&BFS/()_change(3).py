string = input()

# () 개수 - )( 개수 > 0

def solution(p):
    if len(p) == 0:
        return ''
    
    i = 0
    left_count = 0
    right_count = 0
    while i < len(p):
        if p[i] == '(':
            left_count += 1
            i += 1
        elif p[i] == ')':
            right_count += 1
            i += 1
        
        if left_count == right_count:
            break
    
    u = p[:i]
    v = p[i:]
    
    if u.count('()') > u.count(')('):
        return u + solution(v)
    else:
        temp = ''
        temp += '('
        temp += solution(v)
        temp += ')'
        
        u = u[1:-1]
        
        temp2 = ''
        for i in range(len(u)):
            if u[i] == '(':
                temp2 += ')'
            elif u[i] == ')':
                temp2 += '('
        
        return temp + temp2

print(solution(string))