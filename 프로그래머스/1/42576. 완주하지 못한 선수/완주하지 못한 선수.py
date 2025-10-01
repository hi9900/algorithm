def solution(participant, completion):
    participant_map = dict()
    for p in participant:
        if p in participant_map:
            participant_map[p] += 1
        else:
            participant_map[p] = 1
            
    for c in completion:
        participant_map[c] -= 1
        
    for name in participant_map:
        if participant_map[name] == 1:
            return name
