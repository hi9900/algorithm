S = input()
# 지워야 할 0, 1 개수
cnt_zero, cnt_one = S.count('0') // 2, S.count('1') // 2
# 앞에서부터 1 지우기 + 뒤에서부터 0 지우기
cnt = 0
while 1:
    if cnt == cnt_one:
        break
    for i in range(len(S)):
        if S[i] == '1':
            cnt += 1
            S = S[:i] + S[i+1:]
            break

cnt = 0
while 1:
    if cnt == cnt_zero:
        break
    for i in range(len(S)-1, -1, -1):
        if S[i] == '0':
            cnt += 1
            S = S[:i] + S[i + 1:]
            break

print(S)
