# 17세보다 많거나 80kg 이상이면 성인부
while 1:
    name, *data = input().split()

    if name == '#' and data == ['0', '0']:
        break

    if int(data[0]) > 17 or int(data[1]) >= 80:
        result = 'Senior'
    else:
        result = 'Junior'
    print(name, result)
    