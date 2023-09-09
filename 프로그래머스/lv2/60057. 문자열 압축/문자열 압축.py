def solution(s):
    length = len(s)
    answer = length  # 압축하지 않았을 때의 길이를 초기값으로 설정
    
    for step in range(1, length // 2 + 1):  # 1부터 문자열 길이의 절반까지 검사
        compressed = ""
        prev = s[0:step]  # 압축할 문자열 초기값
        count = 1
        
        for j in range(step, length, step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
                
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    
    return answer