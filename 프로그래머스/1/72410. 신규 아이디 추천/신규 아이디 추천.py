def solution(new_id):
    answer = []
    
    for c in new_id:
        # 1. 대문자 -> 소문자: ord + 32
        if 65 <= ord(c) <= 90:
            answer.append(chr(ord(c) + 32))
            continue
        elif 97 <= ord(c) <= 122: 
            answer.append(c)
            continue
        # 2
        if c in '0123456789-_.':
            # 3
            if answer and (c == '.' and answer[-1] == '.'):
                continue
            # 4
            if not answer and c == '.':
                continue
            answer.append(c)

    # 4
    if answer and answer[-1] == '.':
        answer.pop()
    # 5
    if not answer:
        answer = ['a']
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer.pop()
        return ''.join(answer)
    # 7
    if answer and len(answer) <= 2:
        while 1:
            answer.append(answer[-1])
            if len(answer) == 3:
                return ''.join(answer)
    
    return ''.join(answer)