string = "aabbaccc"

length = len(string)

min_length = int(1e9)
for s in range(1, length // 2 + 1):
    i = 0
    array = []
    while(s*i < length):
        array.append(string[s*i:s*(i+1)])
        i += 1
    
    count = 1
    prev = array[0]

    case = []
    for i in range(1, len(array)):
        if array[i] == prev:
            count += 1
        else:
            if count > 1:
                case.append(str(count) + prev)
            else:
                case.append(prev)
            count = 1
            prev = array[i]
    
    if count > 1:
        case.append(str(count) + prev)
    else:
        case.append(prev)
    
    case_length = 0
    for i in range(len(case)):
        case_length += len(case[i])
    
    if case_length < min_length:
        min_length = case_length

print(min_length)