
def solution(s):
    n = len(s)
    answer = n

    for i in range(n // 2, 0, -1):
        prev = s[0:i]
        count = 1
        t = ''
        for j in range(i, n, i):
            if s[j:j + i] == prev:
                count += 1
            else:
                if count > 1:
                    t += str(count)
                t += prev
                count = 1
            prev = s[j:j + i]

        if count > 1:
            t += str(count)
        t += prev

        answer = min(answer, len(t))
    return answer
