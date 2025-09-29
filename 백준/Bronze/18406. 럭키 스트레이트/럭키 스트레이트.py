import sys
input = sys.stdin.readline

n = input().rstrip()
l, r = n[:len(n)//2], n[len(n)//2:]

if sum(map(int, l)) == sum(map(int, r)):
    print('LUCKY')
else:
    print('READY')
