S = input()
N = len(S)

# 연속된 0 또는 1의 묶음 갯수
counts = [0, 0]

# 이전 값
for i in range(1, N):
    # 이전 값과 다르면,
    if S[i-1] != S[i]:
        # 이전 값까지 한 묶음처리
        counts[int(S[i - 1])] += 1

# 마지막 묶음 처리
counts[int(S[N-1])] += 1

# 둘 중 작은 값
print(min(counts))
