import sys
sys.stdin = open("input.txt")


def top(i, k, s, rs):
    global result, B

    # 지금까지 더한 값(s)의 결과(s-B)가 result 보다 크다: ㄴㄴ
    # 지금까지 더한 값(s) + 남은 합(rs)가 B보다 작다: ㄴㄴ
    if (s - B) >= result or s+rs < B:
        return

    # s == B다: result=0
    if s == B or rs == B or s+rs == B:
        e = 1
        result = 0
        return

    # 배열의 끝까지 조사 했는데, s가 B보다 작다: ㄴㄴ
    if i == k and s < B:
        return

    # s가 B보다 크거나 같으면, result s-B 작은값
    if s >= B:
        result = min(result, (s-B))
        return

    top(i + 1, k, s, rs-S[i])
    top(i + 1, k, s+S[i], rs-S[i])


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    result = sum(S)-B
    top(0, N, 0, sum(S))
    print(f"#{tc} {result}")
