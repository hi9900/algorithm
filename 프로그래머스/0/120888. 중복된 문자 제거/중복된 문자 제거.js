function solution(my_string) {
    const s = new Set(my_string);
    return [...s].join('');
}