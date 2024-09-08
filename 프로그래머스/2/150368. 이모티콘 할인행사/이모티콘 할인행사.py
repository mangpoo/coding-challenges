from itertools import product

def solution(users, emoticons):
    
    discount_rate = [10, 20, 30, 40]
    max_plus = 0
    max_sales = 0
    answer = []
    
    for d in product(discount_rate, repeat=len(emoticons)):
        plus = 0
        sales = 0
        for u_rate, u_price in users:
            cost = 0

            for i in range(len(emoticons)):
                if d[i] >= u_rate:
                    cost += emoticons[i] * (100 - d[i]) // 100

            if cost >= u_price:
                plus += 1
            else:
                sales += cost

        if plus > max_plus:
            max_plus = plus
            max_sales = sales
        elif plus == max_plus:
            max_sales = max(max_sales, sales)
            
    answer.append(max_plus)
    answer.append(max_sales) 
    
    return answer