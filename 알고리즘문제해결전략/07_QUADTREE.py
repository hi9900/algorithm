## 7.2 문제: 쿼드 트리 뒤집기([ID: QUADTREE](https://www.algospot.com/judge/problem/read/QUADTREE#))

import sys
sys.stdin = open('./input.txt', 'r')

def solve(s, idx):
    # 문자열을 모두 순회
    if idx == len(s):
        return ""

    c = s[idx]
    if c == 'b':
        return 'b'
    if c == 'w':
        return 'w'

    # x이면, 내부 트리를 상하 반전 후 반환
    idx += 1
    lt = solve(s, idx)
    idx += len(lt)
    rt = solve(s, idx)
    idx += len(rt)
    lb = solve(s, idx)
    idx += len(lb)
    rb = solve(s, idx)
    return f'x{lb}{rb}{lt}{rt}'

T = int(input())
for _ in range(T):
    X = input()

    """
    x (lt) (rt) (lb) (rb) 
    -> 상하반전: x (lb) (rb) (lt) (rt)
    -> 단, 가장 안쪽부터 바깥쪽까지 상하반전 진행
    """

    result = solve(X, 0)
    print(result)