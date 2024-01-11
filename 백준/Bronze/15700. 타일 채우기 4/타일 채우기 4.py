import sys
input = sys.stdin.readline

N, M = map(int, input().split())

"""
1 x N -> N // 2
2 x N " ->  max( (N // 2) * 2 , N)

M x N -> N * M // 2
"""

print(N * M // 2)