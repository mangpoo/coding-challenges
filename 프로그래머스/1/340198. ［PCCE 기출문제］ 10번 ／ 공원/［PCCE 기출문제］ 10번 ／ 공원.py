def solution(mats, park):
    answer = 0  # 최대값을 저장할 변수
    rows = len(park)
    cols = len(park[0])

    mats.sort()  # 작은 돗자리부터 확인하기 위해 오름차순 정렬

    # 모든 돗자리 크기에 대해 검사
    for mat_size in mats:
        for i in range(rows):
            for j in range(cols):
                # 돗자리가 공원을 벗어나지 않는지 확인
                if i + mat_size <= rows and j + mat_size <= cols:
                    all_minus_one = True
                    for x in range(i, i + mat_size):  # mat_size x mat_size 영역의 행 반복
                        for y in range(j, j + mat_size):  # mat_size x mat_size 영역의 열 반복
                            if park[x][y] != "-1":  # 영역 내에 -1이 아닌 값이 있으면
                                all_minus_one = False
                                break
                        if not all_minus_one:
                            break
                    if all_minus_one:  # 영역이 모두 -1이면
                        answer = max(answer, mat_size)  # 최대값 업데이트

    return answer if answer > 0 else -1  # 아무 돗자리도 깔 수 없는 경우 -1 반환
