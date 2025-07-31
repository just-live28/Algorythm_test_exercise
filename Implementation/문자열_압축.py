def solution(s):
    N = len(s)
    
    min_length = N
    for size in range(1, N // 2 + 1):
        word = ''
        cur = s[0:size]
        count = 1
        for i in range(1, N // size + 2):
            token = s[i * size:(i+1) * size]
            
            if cur == token:
                count += 1
            else:
                if count > 1:
                    word += str(count) + cur
                else:
                    word += cur
                cur = token
                count = 1
            
        min_length = min(min_length, len(word))

    return min_length