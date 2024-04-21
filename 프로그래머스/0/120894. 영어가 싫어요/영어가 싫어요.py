def solution(numbers):
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = ''
    
    word = ''
    for i in numbers:
        word += i
        
        if word in number:
            answer += str(number.index(word))
            word = ''
    
    return int(answer)