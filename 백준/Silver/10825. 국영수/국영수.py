import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    (name, K, E, M) = input().split()

    lst.append((name, int(K), int(E), int(M)))

lst = sorted(lst, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for _ in range(N):
    print(lst[_][0])
