function solution(n) {
    var answer = ~~(n / 7) + (n % 7 ? 1 : 0);
    return answer;
}