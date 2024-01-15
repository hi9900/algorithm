S = input()

# 연속된 0 또는 1의 묶음 갯수
cnt = {
    '0': 0,
    '1': 0
}

# 이전 값
before = S[0]

for i in S[1:]:
    # 이전 값과 다르면,
    if i != before:
        # 이전 값까지 한 묶음처리
        cnt[before] += 1
        # 새로운 묶음으로 표시
        before = i

# 마지막 묶음 체크
cnt[before] += 1

# 둘 중 작은 값
print(min(cnt['0'], cnt['1']))