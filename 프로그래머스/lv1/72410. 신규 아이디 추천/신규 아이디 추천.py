
def solution(new_id):
    
    # 1단계
    lower_new_id = new_id.lower()
    
    # 2단계
    lower_new_id2 = ""
    for i in lower_new_id:
        if i.isalpha() or i.isdigit() or i in '-_.':    # isalpha = 알파벳, isdigit = 숫자
            lower_new_id2 += i
    # 3단계
    new_id_list = []
    count = 0
    for i in lower_new_id2:
        if i == '.':
            count += 1
            if count > 1:
                continue
            new_id_list.append(i)
        else:
            new_id_list.append(i)
            count = 0
    new_id_str = ''.join(new_id_list)
    
    # 4단계
    if new_id_str.startswith('.'):      # startswith, endswith 함수 사용
        new_id_str = new_id_str[1:]
        
    if new_id_str.endswith('.'):
        new_id_str = new_id_str[:-1]
        
    # 5단계
    if new_id_str == "":
        new_id_str += "a"
    
    # 6단계
    if len(new_id_str) >= 16:
        new_id_str = new_id_str[:15]
        if new_id_str.endswith('.'):
            new_id_str = new_id_str[:-1]
    # 7단계
    if len(new_id_str) <= 2:
        test_str = new_id_str[-1]
        for i in range(3):
            new_id_str += test_str
            if len(new_id_str) == 3:
                break
    
    return new_id_str
            