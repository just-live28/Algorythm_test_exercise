from bisect import bisect_left, bisect_right

def count_by_range(array, start, end):
    left_index = bisect_left(array, start)
    right_index = bisect_right(array, end)
    return right_index - left_index

def solution(words, queries):
    arr = [[] for i in range(10001)]
    reverse_arr = [[] for i in range(10001)]
    
    for word in words:
        arr[len(word)].append(word)
        reverse_arr[len(word)].append(word[::-1])
    
    for i in range(10001):
        arr[i].sort()
        reverse_arr[i].sort()
    
    answer = []
    for query in queries:
        if query[0] != '?':
            result = count_by_range(arr[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
            answer.append(result)
        else:
            query = query[::-1]
            result = count_by_range(reverse_arr[len(query)], query.replace('?','a'), query.replace('?','z'))
            answer.append(result)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))