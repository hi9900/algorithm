def solution(letter):
    morse = { 
        '.-':'a', '-...':'b', '-.-.':'c', '-..':'d', '.':'e',
        '..-.':'f', '--.':'g', '....':'h', '..':'i', '.---':'j',
        '-.-':'k', '.-..':'l', '--':'m', '-.':'n', '---':'o', 
        '.--.':'p', '--.-':'q', '.-.':'r', '...':'s', '-':'t',
        '..-':'u', '...-':'v', '.--':'w', '-..-':'x', '-.--':'y', '--..':'z'
        }
    
    answer = ''
    let = ''
    for l in letter:
        if l == " ":
            answer += morse[let]
            let = ''
        else:
            let += l
    answer += morse[let]
    
    return answer