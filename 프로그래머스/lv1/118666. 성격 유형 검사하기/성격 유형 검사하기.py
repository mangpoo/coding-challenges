def solution(survey, choices):
    
    mbti_dictionary = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    mbti = [0,3,2,1,0,1,2,3]   
        
    for i in range(len(choices)):
        if(choices[i] < 4):
            mbti_dictionary[survey[i][0]] += mbti[choices[i]]
        elif(choices[i] > 4):
            mbti_dictionary[survey[i][1]] += mbti[choices[i]]

    answer = []
    j = 0
    
    for i in range(0, len(mbti_dictionary), 2):
        
        mbti_key_list = list(mbti_dictionary.keys())
        mbti_value_list = list(mbti_dictionary.values())

        if(mbti_value_list[i] > mbti_value_list[i+1]):
            answer.append(mbti_key_list[i])
        elif(mbti_value_list[i] < mbti_value_list[i+1]):
            answer.append(mbti_key_list[i+1]) 
        else:
            answer.append(mbti_key_list[i])
        
        j += 1
        
    return ''.join(answer)