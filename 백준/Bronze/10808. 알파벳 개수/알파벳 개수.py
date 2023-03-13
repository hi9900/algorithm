S = list(map(str, input()))

# 97 ~ 122: 26
# 1 ~ 26
cnt = [0] * 26
for i in S:
    cnt[ord(i)-97] += 1

print(*cnt)

