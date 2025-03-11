function solution(my_str, n) {
    let answer = [];
    const array = [...my_str]
    
    for(let i=0; i<array.length; i=i+n) {
        answer.push(array.slice(i, i+n).join(""));
    }
    return answer;
}