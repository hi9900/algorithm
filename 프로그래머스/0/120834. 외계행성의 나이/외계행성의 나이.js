function solution(age) {
    const alpha = "abcdefghijklmnopqrstuvwxyz";
    let answer = "";
    [...age.toString()].forEach((v) => {
        answer += alpha[v];
    })
    return answer;
}