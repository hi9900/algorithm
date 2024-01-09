import pprint
import sys
sys.stdin = open('ex8_floyd_input.txt')

INF = int(1e9)

# 노드의 개수 N, 간선의 개수 M
N = int(input())
M = int(input())
# 2차원 리스트를 무한으로 초기화
graph = [[INF] * (N+1) for _ in range(N+1)]
# 자기 자신에게 가는 비용은 0
for i in range(1, N+1):
    graph[i][i] = 0

# 간선에 대한 정보 입력
for _ in range(M):
    # a -> b: c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따른 알고리즘 수행
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
# 결과 출력
for i in range(1, N+1):
    for j in range(1, N+1):
        print('INF', end=" ") if graph[i][j] == INF else print(graph[i][j], end=" ")
    print()

"""
출력 예시
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0
"""
