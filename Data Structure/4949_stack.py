import sys
input = sys.stdin.readline

def isRightString(string):
    q = []
    for s in string:
        if s == '(' or s == '[':
            q.append(s)
        elif s == ')' or s == ']':
            if not q:
                return 'no'
            if s == ')' and q[-1] != '(':
                return 'no'
            if s == ']' and q[-1] != '[':
                return 'no'
            q.pop()
    
    if q:
        return 'no'
    return 'yes' 

while True:
    line = input().rstrip()
    if line == '.':
        break
    
    print(isRightString(line))