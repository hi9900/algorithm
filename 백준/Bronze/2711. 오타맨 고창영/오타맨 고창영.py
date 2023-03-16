import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    idx, word = input().split()
    idx = int(idx)

    print(word[:idx-1], word[idx:], sep="")
