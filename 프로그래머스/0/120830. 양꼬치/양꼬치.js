function solution(n, k) {
    const answer = n * 12000 + (k - ~~(n / 10)) * 2000
    return answer;
}