def solution(phone_book):
    
    phone_book.sort()
    """
    count = 0
    
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[i]) == len(phone_book[j]):
                if(phone_book[i] == phone_book[j]):
                    count = count + 1
            else:
                if(phone_book[i] == phone_book[j][:len(phone_book[i])]):
                    count = count + 1

    if(count > 0):
        answer = False
    else:
        answer = True
        
    return answer
    """
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1][:len(phone_book[i])]:
            return False

    return True
