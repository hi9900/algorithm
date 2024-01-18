N = input()

l = len(N) // 2
front = N[:l]
back = N[l:]

sum_f, sum_b = 0, 0
for i in range(l):
    sum_f += int(front[i])
    sum_b += int(back[i])

print('LUCKY') if sum_f == sum_b else print('READY')
