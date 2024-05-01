import sys
sys.stdin = open('input.txt', 'r')



def match(w, s):
    idx = 0
    while idx < len(s) and idx < len(w) and (w[idx] == '?' or w[idx] == s[idx]):
        idx += 1

    # 패턴 끝에 도달했을 때, 문자열도 끝나면 대응
    if idx == len(w):
        return idx == len(s)
    # *을 만났을 때
    if w[idx] == '*':
        for i in range(0, len(s) - idx + 1):
            if match(w[idx+1:], s[idx+i:]):
                return True
    return False


for _ in range(int(input())):
    W = input()
    result = []
    for _ in range(int(input())):
        file = input()
        if match(W, file):
            result.append(file)

    print(*sorted(result), sep='\n')
