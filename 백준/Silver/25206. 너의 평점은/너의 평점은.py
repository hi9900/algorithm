# 학점 x 과목 평점의 합
result = 0
cnt = 0

# 과목 평점
lst = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0
}

for _ in range(20):
    A, B, C = input().split()
    if C == 'P':
        continue
    cnt += float(B)
    result += lst[C] * float(B)

print(result / cnt)