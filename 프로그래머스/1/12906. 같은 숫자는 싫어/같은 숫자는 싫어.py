def solution(arr):
    answer = []
    for a in arr:
        if not answer:
            answer.append(a)
            continue
        # 마지막 원소와 같으면, 제거
        if answer[-1] == a:
            continue
        answer.append(a)
        
    return answer