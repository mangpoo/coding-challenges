def solution(video_len, pos, op_start, op_end, commands):
    # 시간 문자열을 분과 초로 나누고, 초 단위로 변환
    video_len_min, video_len_sec = map(int, video_len.split(':'))
    time_pos_min, time_pos_sec = map(int, pos.split(':'))
    time_op_start_min, time_op_start_sec = map(int, op_start.split(':'))
    time_op_end_min, time_op_end_sec = map(int, op_end.split(':'))
    
    # 모든 시간을 초 단위로 변환
    video_len_sec_total = video_len_min * 60 + video_len_sec
    time_pos_sec_total = time_pos_min * 60 + time_pos_sec
    time_op_start_sec_total = time_op_start_min * 60 + time_op_start_sec
    time_op_end_sec_total = time_op_end_min * 60 + time_op_end_sec

    result = time_pos_sec_total  # 현재 재생 위치를 설정

    # 명령어 처리
    for command in commands:
        # 먼저 오프닝 구간에 있는지 확인하고, 있으면 오프닝 끝으로 이동
        if time_op_start_sec_total <= result <= time_op_end_sec_total:
            result = time_op_end_sec_total
        
        # 명령어 처리
        if command == 'next':
            result += 10  # 10초 더하기
            if result > video_len_sec_total:  # 비디오 길이를 넘지 않도록 제한
                result = video_len_sec_total
        else:
            result -= 10  # 10초 빼기
            if result < 0:  # 0초보다 작으면 0으로 제한
                result = 0

    # 마지막으로 오프닝 구간에 있는지 확인하고, 있으면 오프닝 끝으로 이동
    if time_op_start_sec_total <= result <= time_op_end_sec_total:
        result = time_op_end_sec_total

    # 초를 다시 분과 초로 변환
    result_min = result // 60
    result_sec = result % 60

    # 결과를 'mm:ss' 형식으로 변환
    result_time = f'{result_min:02}:{result_sec:02}'
    
    return result_time

# 테스트 예시
print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]))  # 예상: "13:00"
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))  # 예상
