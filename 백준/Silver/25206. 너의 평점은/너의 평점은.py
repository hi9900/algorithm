import sys
input = sys.stdin.readline

aver = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0,
}
s=0
s_s = 0
for _ in range(20):
    name, score, rate = map(str, input().split())

    if rate == "P":
        continue

    s += float(score) * aver[rate]
    s_s += float(score)

print(s/s_s)