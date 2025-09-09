import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    max_q = []
    min_q = []
    freq = {}
    for _ in range(n):
        oper, num = input().rstrip().split()
        num = int(num)
        
        if oper == 'I':
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)
            freq[num] = freq.get(num, 0) + 1
        else:
            if not freq:
                continue
            
            if num == -1:
                while min_q:
                    min_num = heapq.heappop(min_q)
                    
                    if freq.get(min_num, 0) > 0:
                        freq[min_num] -= 1
                        
                        if freq[min_num] == 0:
                            del freq[min_num]
                        break
            else:
                while max_q:
                    max_num = -heapq.heappop(max_q)
                    
                    if freq.get(max_num, 0) > 0:
                        freq[max_num] -= 1
                        
                        if freq[max_num] == 0:
                            del freq[max_num]
                        break

    result = sorted(list(freq.keys()))
    if not result:
        print('EMPTY')
    else:
        print(result[-1], result[0])