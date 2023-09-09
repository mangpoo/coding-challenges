from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    counter = Counter()     # 딕셔너리

    for i in orders:
        sorted_orders = sorted(i)    # EX) ACB -> ABC 정렬
        for j in course:
            for z in combinations(sorted_orders, j):
                counter[''.join(z)] += 1
                
    
    for i in course:
        max_count = -1
        best_combinations = []
        for k, v in counter.items():
            if len(k) == i:
                if v > max_count:
                    best_combinations = [k]
                    max_count = v
                elif v == max_count:
                    best_combinations.append(k)
                    
        if max_count >= 2:
            answer.extend(best_combinations)    #   최소 2명 이상의 손님에게서만 받은거 추가
        
    answer.sort()
    
    return answer