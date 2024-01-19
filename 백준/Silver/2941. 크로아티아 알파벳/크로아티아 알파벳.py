import sys
input = sys.stdin.readline

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input().rstrip()

for c in croatia:
    if c in word:
        word = word.replace(c, '1')

print(len(word))