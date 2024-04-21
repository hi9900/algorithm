def solution(s, skip, index):
    answer = ''
    # 알파벳 a ~ z = 0(97) ~ 25(122)
    # skip에 속한 알파벳의 ord값
    skip_o = []
    for c in skip:
        skip_o.append(ord(c) - 97)
    skip_o.sort()
    
    # 1. s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꾼다.
    # 2. z를 넘어가면 a로
    # 3. skip에 속한 알파벳은 제외한다.
    for c in s:
        # index만큼 뒤로
        start = ord(c) - 97
        cnt = 1
        while 1:
            check = (start + cnt) % 26

            if check in skip_o:
                start += 1
            else:
                cnt += 1
            if cnt > index:
                break

            
        answer += chr(97 + check)
        
    return answer