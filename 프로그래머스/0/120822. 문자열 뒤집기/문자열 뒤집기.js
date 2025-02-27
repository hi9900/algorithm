function solution(my_string) {
    return Array.from(my_string).reduce((a, c) => c + a, "");
}