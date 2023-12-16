N = int(input())
# N = 5 # 11475
# 0 <= N <= 23
# 00시 00분 00초 ~ N시 59분 59초 (N+1시 00분 00초)

cnt = 0
# 시
for h in range(N+1):
    # 분
    for m in range(60):
        # 초
        for s in range(60):
            if "3" in str(h) or "3" in str(m) or "3" in str(s):
                cnt += 1

print(cnt)
