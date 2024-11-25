def validate_vps(string):
    while True:
        if len(string) == 0:
            return 'YES'
        
        if string[0] == ')' or string.find(')') == -1:
            break
    
        i = string.find("()")
        string = string[:i] + string[i+2:]
    return 'NO'

n = int(input())

for _ in range(n):
    print(validate_vps(input()))