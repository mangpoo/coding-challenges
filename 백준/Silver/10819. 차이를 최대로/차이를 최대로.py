import itertools

N = int(input(""))
A = list(map(int, input().split()))
sort_A = itertools.permutations(A, len(A))
result = 0
max_permutations_A = None
for i in sort_A:
    sum = 0
    for j in range(len(i) - 1):
        sum += abs(i[j] - i[j + 1])
        if(sum > result):
            result = sum
            max_permutations_A = i



print(result)
