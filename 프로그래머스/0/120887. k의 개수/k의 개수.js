function solution(i, j, k) {
    let answer = 0;
    
    while (i <= j) {
        answer += i.toString().split("")
                    .filter(v => v === k.toString())
                    .length;
        i++;
    }
    
    return answer;
}