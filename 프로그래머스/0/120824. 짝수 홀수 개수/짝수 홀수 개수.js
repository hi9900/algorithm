function solution(num_list) {
    const oddLength = num_list.filter(v => v % 2).length;
    const evenLength = num_list.length - oddLength;
    return [evenLength, oddLength]
}