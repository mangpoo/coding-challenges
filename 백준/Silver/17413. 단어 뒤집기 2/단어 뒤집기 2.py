# 단어 뒤집기 2
S = input("")
result = []
test = []
tag = False

for i in S:
    if i == '<':
        if test:
            result.append(''.join(test[::-1]))
            test = []
        tag = True
        result.append(i)
    elif i == '>':
        tag = False
        result.append(i)
    elif tag:
        result.append(i)
    elif i == ' ':
        if test:
            result.append(''.join(test[::-1]))
            test = []
        result.append(i)
    else:
        test.append(i)

if test:
    result.append(''.join(test[::-1]))

print(''.join(result))