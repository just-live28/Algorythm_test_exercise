from bisect import bisect_left, bisect_right

def solution(words, queries):
    dic = [[] for _ in range(1000001)]
    reverse_dict = [[] for _ in range(1000001)]
    
    # 단어 길이별 리스트에 단어 추가
    for word in set(words):
        dic[len(word)].append(word)
        reverse_dict[len(word)].append(''.join(reversed(list(word))))
    
    # 쿼리 이진 탐색을 위한 단어 길이 별 정렬
    for i in range(2, 1000001):
        dic[i].sort()
        reverse_dict[i].sort()
    
    result = []
    for query in queries:
        size = len(query)
        # 접두사인 경우
        if query[0] == '?':
            reverse_query = ''.join(reversed(list(query)))
            end_idx = bisect_right(reverse_dict[size], reverse_query.replace('?', 'z'))
            start_idx = bisect_left(reverse_dict[size], reverse_query.replace('?', 'a'))
        # 접미사인 경우
        else:
            end_idx = bisect_right(dic[size], query.replace('?', 'z'))
            start_idx = bisect_left(dic[size], query.replace('?', 'a'))

        result.append(end_idx - start_idx)
            
    return result