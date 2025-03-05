function solution(numbers, direction) {
    const answer = [...numbers, ...numbers];
    let start = 1;

    if (direction === "right") {
        start = numbers.length - 1;
    }
    let end = start + numbers.length;
    
    return answer.slice(start, end);
}