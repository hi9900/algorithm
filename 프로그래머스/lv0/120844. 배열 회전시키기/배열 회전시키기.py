def solution(numbers, direction):

    if direction[0] == "r":
        return numbers[-1], *numbers[:-1]
        return
    else:
        return *numbers[1:], numbers[0]
        return