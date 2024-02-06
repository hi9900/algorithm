def solution(v):
    ans = [0, 0]
    for vx, vy in v:
        ans[0] ^= vx
        ans[1] ^= vy
    
    return ans