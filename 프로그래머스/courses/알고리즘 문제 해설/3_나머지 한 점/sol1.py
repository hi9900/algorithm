def solution(v):
    check_x = []
    check_y = []
    
    # 없으면 추가하고, 있으면 지움
    for vx, vy in v:
        if vx in check_x:
            check_x.remove(vx)
        else:
            check_x.append(vx)
        if vy in check_y:
            check_y.remove(vy)
        else:
            check_y.append(vy)
    
    answer = [check_x[0], check_y[0]]
    return answer