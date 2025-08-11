def solution(s):
    is_start = True
    ans = ''
    for c in s:
        if c.isalpha():
            if is_start:
                ans += c.upper()
            else:
                ans += c.lower()
            is_start = False

        elif c == ' ':
            is_start = True
            ans += c
        else:
            is_start = False
            ans += c

    return ans