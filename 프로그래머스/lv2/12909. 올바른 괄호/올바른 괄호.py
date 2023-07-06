#스택 사용하기

def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:  
                return False
            stack.pop()  
    return len(stack) == 0