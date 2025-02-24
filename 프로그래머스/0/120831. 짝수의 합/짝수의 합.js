function solution(n) {
    let answer = 0;
    for (i=0; i<=n; i++) {
        if (i % 2 !== 0) continue;
        answer += i;
    }
    return answer;
}