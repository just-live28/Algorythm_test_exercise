from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

array = [[] for _ in range(100001)]
reverse_array = [[] for _ in range(100001)]

def count_target(array, start, end):
    left = bisect_left(array, start)
    right = bisect_right(array, end)
    
    return right - left

for word in words:
    length = len(word)
    
    array[length].append(word)
    reverse_array[length].append(word[::-1])

for i in range(100001):
    array[i].sort()
    reverse_array[i].sort()

results = []
for query in queries:
    length = len(query)
    
    if query[0] == '?':
        query = query[::-1]
        
        start_word = query.replace('?', 'a')
        end_word = query.replace('?', 'z')
        
        result = count_target(reverse_array[length], start_word, end_word)
        
        results.append(result)
    else:
        start_word = query.replace('?', 'a')
        end_word = query.replace('?', 'z')
        
        result = count_target(array[length], start_word, end_word)
        
        results.append(result)

print(results)