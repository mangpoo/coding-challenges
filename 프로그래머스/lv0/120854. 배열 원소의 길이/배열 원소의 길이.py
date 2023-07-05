def solution(strlist):
    
    len_strlist = [0] * len(strlist)
    
    for i in range(len(strlist)):
        len_strlist[i] = len(strlist[i])
    
    return len_strlist