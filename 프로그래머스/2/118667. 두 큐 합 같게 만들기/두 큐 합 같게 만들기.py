from collections import deque

def solution(queue1, queue2):
    # 큐 합 계산
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    # 전체 합이 홀수라면 균등하게 나눌 수 없으므로 -1 반환
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    target_sum = (sum1 + sum2) // 2  # 각 큐가 가져야 할 목표 합

    # deque로 변환하여 효율적인 pop, append 연산 수행
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    total_operations = 0  # 작업 횟수
    max_operations = len(queue1) * 3  # 최대 작업 횟수 제한 (무한 루프 방지)
    
    # 두 포인터를 사용하여 queue1과 queue2에서 값을 빼면서 합을 맞춰나감
    while sum1 != target_sum and total_operations <= max_operations:
        if sum1 > target_sum:  # queue1의 합이 목표보다 크면 값을 빼서 queue2로 보냄
            value = queue1.popleft()
            sum1 -= value
            queue2.append(value)
            sum2 += value
        else:  # queue1의 합이 목표보다 작으면 queue2에서 값을 빼서 queue1으로 보냄
            value = queue2.popleft()
            sum2 -= value
            queue1.append(value)
            sum1 += value
        
        total_operations += 1  # 작업 횟수 증가

    # 작업 완료 후 각 큐의 합이 같으면 total_operations 반환, 아니면 -1
    if sum1 == target_sum:
        return total_operations
    else:
        return -1
