def solution(progresses, speeds):
    N = len(progresses)
    answer = []
    
    fin = []    
    for i in range(N):
        x, y = divmod((100 - progresses[i]), speeds[i])
        if y == 0:
            fin.append(x)
        else:
            fin.append(x+1)
    
    cnt = 1
    s = fin[0]
    for i in range(1, N):
        if s >= fin[i]:
            cnt += 1
        else:
            print(cnt, s)
            answer.append(cnt)
            cnt = 1
            s = fin[i]
    answer.append(cnt)
    return answer