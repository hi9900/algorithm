function solution(order) {
    return [...order.toString()].reduce((a, c) => "369".includes(c) ? a + 1 : a, 0);
}