## 노예취용테스트

import sys

테스트케이스 = int(input())

for _ in range(테스트케이스):
    명 = int(sys.stdin.readline().strip())
    사원들 = []

    for _ in range(명):
        뇌지컬점수, 면접점수 = map(int, sys.stdin.readline().split())
        사원들.append((뇌지컬점수, 면접점수))

    사원들.sort()

    합격 = 0
    다른사원면접순위 = 100001


    for _, 면접순위 in 사원들:
        if 면접순위 < 다른사원면접순위:
            합격 += 1
            다른사원면접순위 = 면접순위

    print(합격)

