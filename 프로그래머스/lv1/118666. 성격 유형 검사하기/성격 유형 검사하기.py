def solution(survey, choices):
    
    mbti_dictionary = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}     # 지표생성
    mbti = [0,3,2,1,0,1,2,3]    # 선택지 점수
        
    for i in range(len(choices)):   # 지표에 알파벳마다 나오는 결과 점수를 누적 
        if(choices[i] < 4):
            mbti_dictionary[survey[i][0]] += mbti[choices[i]]
        elif(choices[i] > 4):
            mbti_dictionary[survey[i][1]] += mbti[choices[i]]

    answer = []
    j = 0
    
    for i in range(0, len(mbti_dictionary), 2):     # 1 ~ 4번지표 검사 결과 비교 (알파벳4글자까지만)
        
        mbti_key_list = list(mbti_dictionary.keys())
        mbti_value_list = list(mbti_dictionary.values())

        if(mbti_value_list[i] > mbti_value_list[i+1]):      
            answer.append(mbti_key_list[i])                 # 비교한 값 answer리스트에 저장
        elif(mbti_value_list[i] < mbti_value_list[i+1]):
            answer.append(mbti_key_list[i+1]) 
        else:
            answer.append(mbti_key_list[i])
        
        j += 1
        
    return ''.join(answer)