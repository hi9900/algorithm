function solution(s) {
    return [...s].filter(v => s.split(v).length === 2).sort().join("");
}