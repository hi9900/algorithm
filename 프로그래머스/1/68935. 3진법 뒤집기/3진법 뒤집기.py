def switch(n, a):
    result = ''
    
    while n >= a:
        n, x = divmod(n, a)
        result += str(x)
    result += str(n)

    return result
    
def solution(n):
    return int(switch(n, 3), 3)
    