import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    private static int[][] board = new int[5][5];
    private static Set<Integer> uniqueNumbers = new HashSet<>();
    private static int[] dx = {0, 1, 0, -1}; // 상하좌우 이동을 위한 x축 변화량
    private static int[] dy = {1, 0, -1, 0}; // 상하좌우 이동을 위한 y축 변화량

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // 숫자판 입력 받기
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                board[i][j] = scanner.nextInt();
            }
        }
        
        // 모든 칸에서 시작해 DFS 실행
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                dfs(i, j, 0, 0);
            }
        }
        
        // 결과 출력
        System.out.println(uniqueNumbers.size());
        scanner.close();
    }

    private static void dfs(int x, int y, int depth, int number) {
        if (depth == 6) { // 6자리 수 완성
            uniqueNumbers.add(number);
            return;
        }
        
        // 네 방향으로 탐색
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            // 범위 확인
            if (nx >= 0 && nx < 5 && ny >= 0 && ny < 5) {
                dfs(nx, ny, depth + 1, number * 10 + board[nx][ny]);
            }
        }
    }
}