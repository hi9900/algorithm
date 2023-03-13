import sys
input = sys.stdin.readline

N = int(input())
call = list(map(int, input().split()))

Young = 0
Min = 0
for i in range(N):    
    Young += 10 * (call[i]//30) + 10
    Min += 15 * (call[i]//60) + 15

if Young < Min:
    print("Y", Young)
elif Young > Min:
    print("M", Min)
else:
    print("Y M", Young)