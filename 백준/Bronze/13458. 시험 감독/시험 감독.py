import sys
input = sys.stdin.readline

"""
총감독관 -> B명
부감독관 -> C명 * n
"""
N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0

for i in range(N):
    # 총 감독관이 모두 감독을 하고도 남는 경우 고려
    if lst[i] < B:
        cnt += 1
    elif (lst[i] - B) % C:
        cnt += (lst[i] - B) // C + 2
    else:
        cnt += (lst[i] - B) // C + 1

print(cnt)
