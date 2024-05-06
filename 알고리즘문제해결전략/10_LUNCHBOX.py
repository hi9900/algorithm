import sys
sys.stdin = open('input.txt', 'r')

# https://algospot.com/judge/problem/read/LUNCHBOX

for _ in range(int(input())):
    n = int(input())
    heating_time = list(map(int, input().split()))
    eating_time = list(map(int, input().split()))

    lunchbox = list(zip(heating_time, eating_time))
    lunchbox.sort(key=lambda x: (-x[1], x[0]))
    ans = 0
    fin_heat = 0
    for h, e in lunchbox:
        fin_heat += h
        ans = max(fin_heat + e, ans)

    print(ans)