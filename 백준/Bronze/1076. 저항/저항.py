value = {
    'black' : '0',
    'brown' : '1',
    'red'	: '2',
    'orange': '3',
    'yellow': '4',
    'green'	: '5',
    'blue'	: '6',
    'violet': '7',
    'grey'	: '8',
    'white'	: '9',
}

A = input()
B = input()
C = input()
result = f'{value[A]}{value[B]}{int(value[C]) * "0"}'

print(int(result))
