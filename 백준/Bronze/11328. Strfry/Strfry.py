import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    A, B = input().split()

    for c in A:
        if c in B and A.count(c) == B.count(c):
            pass
        else:
            print("Impossible")
            break
    else:
        print("Possible")
            
            
