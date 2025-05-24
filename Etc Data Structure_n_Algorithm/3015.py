n = int(input())
stk = []

count = 0
for _ in range(n):
    h = int(input())
    cnt = 1

    while stk:
        top_h, top_c = stk[-1]
        if top_h < h:
            count += top_c
            stk.pop()
        elif top_h == h:
            count += top_c
            cnt += top_c
            stk.pop()
        else:
            count += 1
            break
    stk.append([h, cnt])
    
print(count)