def switch(mode):
    if mode == 0:
        return 1
    return 0
    
def solution(code):
    ret = ''
    mode = 0
    
    n = len(code)
    for i in range(n):
        if code[i] == '1':
            mode = switch(mode)
        elif mode == 0 and i % 2 == 0:
            ret += code[i]
        elif mode == 1 and i % 2:
            ret += code[i]
    
    if ret == '':
        return 'EMPTY'
    return ret