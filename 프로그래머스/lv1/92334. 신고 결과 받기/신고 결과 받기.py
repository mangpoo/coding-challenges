from collections import Counter

def solution(id_list, report, k):
    #
    result = [0] * len(id_list)
    revised_report = {}
    set_report = set(report)
    #        
    for i in set_report:
        key, value = i.split(" ")
        if key in revised_report:
            revised_report[key].append(value) # 값을 리스트에 추가
        else:
            revised_report[key] = [value]
            
    # value들만 추출해서 하나의 리스트로 만들기
    all_values = []
    for values in revised_report.values():
        all_values.extend(values)

    # Counter를 이용하여 중복된 value의 개수 구하기
    value_counts = Counter(all_values)   
    #
    k_value_counts = {}
    for key, count in value_counts.items():
        if count >= k:
            k_value_counts[key] = count
    #        
    id_index_map = {id: index for index, id in enumerate(id_list)}
    for key in k_value_counts.keys():
        for i, j in revised_report.items():
            if key in j:
                result[id_index_map[i]] += 1
            
    return result
    