from itertools import combinations
from collections import Counter

def solution(orders, course):
    orders.sort(key=lambda x: len(x))
    answer = []
    for c in course:
        arr = []
        for i in range(len(orders)):
        # order[i]로 만들 수 있는 부분집합
            tmp_course = list(combinations(orders[i], c))
            for j in tmp_course:
                arr.append("".join(sorted(j)))
        # 빈도 순 정렬
        count_arr = Counter(arr).most_common()

        for a, cnt in count_arr:
            # 최고 빈도랑 같은 것만 추가
            if cnt >= 2 and cnt == count_arr[0][1]:
                answer.append(a)
            elif cnt < 2:
                break
                
    return sorted(answer)


    """
    # arr, cnt
    arr = sorted(list(arr), key=lambda x: (len(x), x))
    # print(orders)
    # print(arr)
    answer = []
    
    tmp, t_cnt = [], 0
    
    # arr 값이 orders 안에 2개 이상 포함되면, 코스요리 만들기
    for a in arr:
        cnt = 0
        for order in orders:
            if len(order) < len(a):
                continue
            # 모든 a가 order에 들어있어야 함
            for _a in a:
                if _a not in order:
                    break
            else:
                cnt += 1
        
        # 같은 길이의 코스요리 중 가장 빈도수가 높은 메뉴를 올려야함(질문하기 참고함)
        if cnt >= 2 and not tmp:
            tmp.append(a)
            t_cnt = cnt
        # 새로운 길이의 코스이면, 이전 길이를 모두 추가하고 바꾸기
        elif cnt >= 2 and tmp and len(a) != len(tmp[0]):
            for t in tmp:
                answer.append(t) 
            tmp, t_cnt = [a], cnt
        # 같은 길이의 코스이면, 길이를 비교해서 더 큰거로 바꾸기
        elif cnt >= 2 and tmp and len(a) == len(tmp[0]):
            if t_cnt < cnt:
                tmp, t_cnt = [a], cnt
            # 같은 길이면 추가
            elif t_cnt == cnt:
                tmp.append(a)  
    # 마지막 길이 추가
    for t in tmp:
        answer.append(t) 
        
    return sorted(answer)"""