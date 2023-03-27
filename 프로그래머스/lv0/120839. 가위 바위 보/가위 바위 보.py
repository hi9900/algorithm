def solution(rsp):
    answer = ''
    win = "025"
    for c in rsp:
        answer += win[win.index(c)-1]
    return answer