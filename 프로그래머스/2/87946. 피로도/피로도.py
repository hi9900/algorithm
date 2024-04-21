from itertools import permutations

def solution(k, dungeons):
    answer = 0
    N = len(dungeons)
    
    for permutation in permutations(dungeons, N):
        cnt, kk = 0, k
        for dungeon in permutation:
            if dungeon[0] <= kk:
                kk -= dungeon[1]
                cnt += 1
            if kk <= 0:
                break
                
        answer = max(cnt, answer)
    
    return answer