def solution(s):
    N = len(s)

    min_len = N
    cnt = 1
    for i in range(N // 2, 0, -1):
        c_word = ''
        # 맨 앞 자른거
        key = s[0:i]
        # print(key, end=" -> ")

        # 단위 별로 자르기
        for j in range(i, N, i):
            if len(c_word) >= min_len:
                break

            # 압축
            if key == s[j:j + i]:
                cnt += 1

            # 다른게 나오면, 이전 값 압축 표현 후 갱신
            else:
                if cnt == 1:
                    c_word += key
                else:
                    c_word += f'{cnt}{key}'
                key = s[j:j + i]
                cnt = 1

        # 마지막 잘린 거 더하기
        if cnt == 1:
            c_word += key
        else:
            c_word += f'{cnt}{key}'

        # print(c_word)
        min_len = min(min_len, len(c_word))
    return min_len


print(solution('abcabcabcabcdededededede'))