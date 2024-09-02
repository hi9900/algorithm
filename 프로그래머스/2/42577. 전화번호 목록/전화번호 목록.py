def solution(phone_book):
    # 1. 정렬
    phone_book.sort()
    # 2. i-1 번째 전화번호가 i번째 전화번호의 접두어이면, false
    for i in range(1, len(phone_book)):
        n, m = len(phone_book[i-1]), len(phone_book[i])
        if n > m:
            continue
        if phone_book[i-1] == phone_book[i][:n]:
            return False
    return True