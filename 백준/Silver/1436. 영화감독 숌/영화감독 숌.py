n = int(input())

num = 666

count = 0

while 1:
    if '666' in str(num):
        count += 1
        if n == count:
            break
        else:
            num += 1

    else:
        num += 1

print(num)
    
