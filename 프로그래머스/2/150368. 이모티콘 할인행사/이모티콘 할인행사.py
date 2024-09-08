from itertools import product

def solution(users, emoticons):
    
    discount_rate = [10, 20, 30, 40]
    max_plus = 0
    max_sales = 0
    answer = []
    
    for d in product(discount_rate, repeat=len(emoticons)):
        emoticon_plus = 0
        sales = 0
        for user_rate, user_price in users:
            sum = 0

            for i in range(len(emoticons)):
                if d[i] >= user_rate:
                    sum += emoticons[i] * (100 - d[i]) // 100

            if sum >= user_price:
                emoticon_plus += 1
            else:
                sales += sum

        if emoticon_plus > max_plus:
            max_plus = emoticon_plus
            max_sales = sales
        elif emoticon_plus == max_plus:
            max_sales = max(max_sales, sales)
            
    answer.append(max_plus)
    answer.append(max_sales) 
    
    return answer