from collections import deque

def solution(queue1, queue2):

    sum_queues = (sum(queue1) + sum(queue2)) // 2

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum_queue1 = sum(queue1)
    sum_queue2 = sum(queue2)

    result = 0  
    cut = len(queue1) + len(queue2) + 2  # 무한루프 컷용

    while sum_queue1 != sum_queues:
        if sum_queue1 > sum_queues:
            value = queue1.popleft()
            sum_queue1 -= value
            queue2.append(value)
            sum_queue2 += value
        else:
            value = queue2.popleft()
            sum_queue2 -= value
            queue1.append(value)
            sum_queue1 += value

        result += 1

        if result > cut:
            return -1

    return result
