function solution(n) {
    return Array(n).fill()
            .map((_, index) => index+1)
            .filter(v => v % 2 === 0)
            .reduce((a, c) => a + c, 0);
}