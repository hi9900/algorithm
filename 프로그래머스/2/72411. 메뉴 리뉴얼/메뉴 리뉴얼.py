from itertools import combinations

def solution(orders, course):
    arr = set()
    orders.sort(key=lambda x: len(x))
    
    for i in range(len(orders)):
        # order[i]로 만들 수 있는 부분집합
        # 부분집합의 크기는 course의 값
        for c in course:
            tmp_course = list(combinations(orders[i], c))
            
            for j in tmp_course:
                # 아직 후보임
                arr.add("".join(sorted(j)))
    # arr, cnt
    arr = sorted(list(arr), key=lambda x: (len(x), x))
    # print(orders)
    # print(arr)
    answer = []
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
            
        # 같은 길이의 코스요리 중 가장 빈도수가 높은 메뉴를 올리기(질문하기 참고함)
        # 이미 arr는 길이 순으로 정렬되었음
        if cnt >= 2:
            # 맨 처음 넣기
            if not answer:
                answer.append((a, cnt))
            # 새로운 길이의 코스이면, 일단 넣기
            elif answer and len(answer[-1][0]) != len(a):
                answer.append((a, cnt))
                continue
            # 같은 길이고, 이전에 넣은 cnt보다 크면 교체
            elif answer and len(answer[-1][0]) == len(a) and answer[-1][1] < cnt:
                while answer and len(answer[-1][0]) == len(a) and answer[-1][1] < cnt:
                    answer.pop()
                answer.append((a, cnt))
            # 같은 길이고, cnt가 같으면 같이 넣기
            elif answer and len(answer[-1][0]) == len(a) and answer[-1][1] == cnt:
                answer.append((a, cnt))
        # 개더러움 ㄷㄷ
        
    make = list(zip(*answer))
    return sorted(list(make[0]))