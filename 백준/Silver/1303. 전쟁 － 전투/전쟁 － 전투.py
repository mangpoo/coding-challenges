# 워

from collections import deque

n, m = map(int, input().split())
battleground = []

for _ in range(m):
    solider = list(input().strip())  # 문자열을 리스트로 변환 (런타임에러)
    battleground.append(solider)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y, team, visited):
    queue = deque([(start_x, start_y)])
    visited.add((start_x, start_y))
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                if battleground[nx][ny] == team:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    count += 1

    return count

visited = set()

friendly_power = 0
enemy_power = 0

for i in range(m):
    for j in range(n):
        if (i, j) not in visited:
            if battleground[i][j] == "W":
                friendly_power += bfs(i, j, "W", visited) ** 2
            elif battleground[i][j] == "B":
                enemy_power += bfs(i, j, "B", visited) ** 2

print(friendly_power, enemy_power)