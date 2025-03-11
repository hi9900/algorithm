function solution(array, n) {
    let minDiff = Infinity;
    let answer;
    array = array.sort((a, b) => a - b);
    for (let i of array) {
        let diff = Math.abs(n - i);
        if (diff < minDiff) {
            minDiff = diff;
            answer = i;
        }
    }
    return answer;
}