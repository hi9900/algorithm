import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rooms = {}
# 회의실 이름 입력
for _ in range(N):
    room_name = input().rstrip()
    rooms[room_name] = []
# 예약 시간 입력
for _ in range(M):
    r, s, t = input().split()
    s = int(s)
    t = int(t)
    rooms[r].append((s, t))

cnt = 0
# 회의실 사전순으로 확인
for room in sorted(rooms.keys()):
    cnt += 1
    # 예약 시작 시각은 09-18
    reserve = [1] * 9 + [0] * 9 + [1]
    
    times = sorted(rooms[room])
    for time in times:
        s, t = time
        if reserve[s] == 0:
            for i in range(s, t):
                reserve[i] = 1

    result = []
    start, end = 0, 0
    for i in range(9, 19):
        # 0으로 시작할 때 예약 시작 가능
        if reserve[i-1] == 1 and reserve[i] == 0:
            start = i
        # 1을 만나면, 1인 시간까지 사용가능
        elif reserve[i-1] == 0 and reserve[i] == 1:
            end = i

        if 0 < start and 0 < end:
            result.append((start, end))
            start, end = 0, 0

    print(f'Room {room}:')
    if len(result) == 0:
        print(f'Not available')
    else:
        print(f'{len(result)} available:')
        for s, e in result:
            print(f'{s:02d}-{e:02d}')
    if cnt < N:
        print('-----') 
