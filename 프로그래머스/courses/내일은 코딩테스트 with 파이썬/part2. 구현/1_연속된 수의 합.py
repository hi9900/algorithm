def solution(num, total):
    answer = []
    
    # 연속된 수 n개의 합 = (start + end) * n / 2
    s = 0
    while 1:
        result = (s + s + num - 1) * num / 2
        if result == total:
            return list(range(s, s+num))
        elif result > total:
            s -= 1
        else:
            s += 1
