def solution(wallpaper):
    
    result = []
    width_shap = []
    for i in wallpaper:
        j = i.find("#")
        if(j != -1):
            width_shap.append(j)
    width = min(width_shap)

    length = 0
    for i in wallpaper:
        for j in range(len(i)):
            if i[j] == "#":
                break
        else:
            length += 1
            continue  # 'else'가 실행되면 'continue'로 다음 이터레이션으로 이동
        break  # 'break'가 실행되면 이곳으로 이동, 외부 루프 종료
        
    print(length)  
    print(width)
          
    length1 = 0
    for i in reversed(wallpaper):
        for j in range(len(i)):
            if i[j] == "#":
                break
        else:
            length1 += 1
            continue  # 'else'가 실행되면 'continue'로 다음 이터레이션으로 이동
        break  # 'break'가 실행되면 이곳으로 이동, 외부 루프 종료
    end_length = len(wallpaper) - length1
    
    print(end_length)
    
    width_shap1 = []
    for i in wallpaper:
        j = i.rfind("#")    # 마지막으로 나타나는 # 문자의 위치를 나타냄
        if(j != -1):
            width_shap1.append(j)
    width1 = max(width_shap1) + 1
    
    print(width1)
    
    result.append(length)
    result.append(width)
    result.append(end_length)
    result.append(width1)
    
    return result