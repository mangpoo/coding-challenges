from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    counter = Counter()

    # 모든 주문에 대해 가능한 조합을 생성하고 카운트
    for order in orders:
        sorted_order = sorted(order)
        for c in course:
            for comb in combinations(sorted_order, c):
                counter[''.join(comb)] += 1

    # 각 코스 크기별로 가장 많이 주문된 조합을 찾음
    for c in course:
        max_count = -1
        best_combinations = []
        for comb, count in counter.items():
            if len(comb) == c:
                if count > max_count:
                    best_combinations = [comb]
                    max_count = count
                elif count == max_count:
                    best_combinations.append(comb)

        # 가장 많이 주문된 조합이 2번 이상 주문되었다면 answer에 추가
        if max_count >= 2:
            answer.extend(best_combinations)

    return sorted(answer)