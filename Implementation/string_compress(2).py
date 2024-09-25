s = 'a'

min_length = int(1e9)
for l in range(1, len(s)+1):
    array = []
    
    if len(s) // l == 1:
        continue
    
    index = 0
    for i in range(len(s) // l):
        array.append(s[i * l: (i+1) * l])
        index = (i+1) * l
    remain = s[index:]
    if s[index:] != '':
        array.append(remain)
    
    prev = array[0]
    times = 1
    
    result = []
    for i in range(1, len(array)):
        if array[i] == prev:
            times += 1
        else:
            if times > 1:
                result.append(str(times) + prev)
            else:
                result.append(prev)
            
            prev = array[i]
            times = 1
    if times > 1:
        result.append(str(times) + prev)
    else:
        result.append(prev)

    result = len(''.join(result))

    if result < min_length:
        min_length = result
            
if len(s) == 1:
    print(1)
else:
    print(min_length)
        
    
    
    
    