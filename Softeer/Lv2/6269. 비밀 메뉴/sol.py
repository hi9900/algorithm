import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
secret = ''.join(input().split())
buttons = ''.join(input().split())

# 비밀 메뉴가 조작에 포함되어 있으면 식권을 받을 수 있다.
print('secret') if secret in buttons else print('normal')
