N = input()

l, r = N[:len(N)//2], N[len(N)//2:]

if sum(map(int, l)) == sum(map(int, r)):
    print('LUCKY')
else:
    print('READY')
