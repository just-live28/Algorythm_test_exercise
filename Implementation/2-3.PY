s = "ababcdcdababcdcd"

# 1부터 len(문자열) // 2 까지(끝값 포함)
# unit이 1일때 마지막 요소 제외할 것
max_unit = len(s) // 2

min_length = len(s)
for unit in range(1, max_unit + 1):
    arr = [s[unit * i : unit * (i+1)] for i in range(len(s) // unit + 1)]
    if arr[-1] == "":
        arr.pop()
    
    result = ""
    count = 1
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == prev:
            count += 1
        else:
            if count > 1:
                result += str(count) + prev
            else:
                result += prev
            prev = arr[i]
            count = 1
    
    if arr[-1] == prev:
        if count > 1:
            result += str(count) + prev
        else:
            result += prev
    else:
        result += arr[-1]
    
    min_length = min(min_length, len(result))
