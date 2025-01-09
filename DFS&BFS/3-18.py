def check_index(p):
    i = 0
    count = 0
    while True:
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        i += 1
        
        if count == 0:
            return i
    

p = '(())()'

index = check_index(p)

print(p[1:-1])
