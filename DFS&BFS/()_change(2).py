# 균형이 맞는 시점에서 index를 반환하는 함수 -> u(균형)와 v로 분리
# 올바른 괄호 문자열인지를 검사하는 함수

def find_index(string):
    count = 0
    index = 0
    while True:
        if string[index] == '(':
            count += 1
        else:
            count -= 1
        
        if count == 0:
            return index + 1
        
        index +=1

def is_correct(string):
    if string.count('()') - string.count(')(') > 0:
        return True
    else:
        return False

def solution(p):
    if len(p) == 0:
        return ''
    
    i = find_index(p)
    u, v = p[:i], p[i:]
    
    if is_correct(u):
        return u + solution(v)
    else:
        temp1 = ''
        temp1 += '('
        temp1 += solution(v)
        temp1 += ')'
        
        temp2 = ''
        for i in range(1, len(u)-1):
            if u[i] == '(':
                temp2 += ')'
            else:
                temp2 += '('
                
        return temp1 + temp2