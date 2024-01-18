import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
    word = input().rstrip()
    stack = []
    # 연속된 문자가 아니고, 이전에 나온 문자이면 ㄴㄴ
    for i in word:
        if not stack or i not in stack:
            stack.append(i)
        # 연속된 문자
        elif stack and i in stack and stack[-1] == i:
            continue
        # 연속된 문자가 아니고, 이전에 나온 문자
        else:
            break
    else:
        cnt += 1

print(cnt)
