# 로또
import itertools

while True:
    input_line = input().strip()
    if input_line == "0":
        break

    input_list = list(map(int, input_line.split()))
    K = input_list[0]
    S = input_list[1:]

    result = list(itertools.combinations(S, 6))

    for i in result:
        for j in range(len(i)):
            print(i[j], end = " ")
        print()
    print()