def check(check_word):
    cnt = 0
    for c in check_word:
        if c in 'aeiou':
            cnt += 1

    if 1 <= cnt <= L-2:
        return True
    return False


# 알파벳 소문자들에서 L개를 뽑기
def solve(i, word):
    global result
    if len(word) == L:
        # 모음 1개, 자음 2개 이상 체크
        if check(word):
            print(word)
            # result.add(word)
        return

    if i >= C:
        return

    solve(i+1, word + alpha[i])
    solve(i+1, word)


L, C = map(int, input().split())
alpha = sorted(list(input().split()))
result = set()
solve(0, '')