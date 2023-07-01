from collections import Counter

def solution(participant, completion):
    
    #fail_participant = [p for p in participant if p not in completion or completion.remove(p)]
    
    #return fail_participant[0]

    counter = Counter(participant) - Counter(completion)
    fail_participant = list(counter.keys())[0]
    
    return fail_participant