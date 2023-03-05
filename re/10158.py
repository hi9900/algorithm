# https://www.acmicpc.net/problem/10158
import sys
input = sys.stdin.readline
///////
# 오벽: 오위-왼위/ 오밑-왼밑,
# j == w
# 왼벽: 왼밑-오밑/ 왼위-오위
# j == 0

# 위벽: 왼위-왼밑/ 오위-오밑,
# i == 0
# 밑벽: 오밑-오위/ 왼밑-왼위,
# i == h

w, h = map(int, input().split())
p, q = map(int, input().split())
si, sj = h-q, p
t = int(input())

# 오-위-왼-밑
ant_c = ((-1, 1), (-1, -1), (1, -1), (-1, -1),)

#

while t != 0:
    t -= 1



print(si, sj)