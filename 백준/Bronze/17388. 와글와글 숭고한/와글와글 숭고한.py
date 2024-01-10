lst = list(map(int, input().split()))
name = ['Soongsil', 'Korea', 'Hanyang']
if sum(lst) >= 100:
    print('OK')
else:
    print(name[lst.index(min(lst))])