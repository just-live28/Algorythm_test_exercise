def cal_score(string):
    q = []
    temp = 1
    result = 0
    
    for i in range(len(string)):
        if string[i] == '(':
            q.append(string[i])
            temp *= 2
        elif string[i] == '[':
            q.append(string[i])
            temp *= 3
        elif string[i] == ')':
            if not q or q[-1] != '(':
                return 0
            if string[i-1] == '(':
                result += temp
            q.pop()
            temp //= 2
        elif string[i] == ']':
            if not q or q[-1] != '[':
                return 0
            if string[i-1] == '[':
                result += temp
            q.pop()
            temp //= 3
            
    if q:
        return 0
    else:
        return result

string = input()
print(cal_score(string))