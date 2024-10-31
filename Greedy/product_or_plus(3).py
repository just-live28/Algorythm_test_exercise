# total(앞 수)이 0 또는 1이면 더하는 게 이득
# 뒷 수가 0또는 1이면 더하는 게 이득

s = input()

total = 0
for i in range(len(s)):
    number = int(s[i])
    
    if total == 0 or total == 1:
        total += number
        continue
    
    if number == 0 or number == 1:
        total += number
    else:
        total *= number

print(total)