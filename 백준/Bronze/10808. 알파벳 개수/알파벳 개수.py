import sys
input = sys.stdin.readline

arr = [0] * 26

word = input().rstrip()
for c in word:
    arr[ord(c) - 97] += 1

print(*arr)