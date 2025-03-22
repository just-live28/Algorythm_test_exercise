def print_hello(k):
    if k == 0:
        return ""
    str = 'HELLO'
    
    return str + print_hello(k-1)
    print(">>")
    print_hello(k-1)
    
print_hello(1)


def mult(a, b):
    if b == 0:
        return 0
    return a + mult(a, b-1)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(a % b, a)
    
        
1 * 0 = 0
1 * 1  =1


def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)
    
sum(0)


1 * 2...nb
def expt(a, b):
    if b == 0:
        return 1
    half = expt(a, b // 2)
    
    if b % 2 == 1:
        return a * 
    


f(x-1) + f(x-2) + f(x-3)    
    
def count(ls, n, s, index, sum):
    
    if index == n:
        return 0
    
    new_sum = ls[index] + sum
    if new_sum == s:
        return 1
    
    return count(ls, n, s, index+1, new_sum) + count(ls, n , s, index+1, sum)
    

expt(2, 0)