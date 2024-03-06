import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }

        int low = 0;
        int high = 10000; // 문제 조건에 따라 배열에 들어있는 수는 최대 10,000
        int result = high;

        while (low <= high) {
            int mid = (low + high) / 2;
            int groups = 1; // 현재 구간의 개수
            int min = array[0], max = array[0]; // 현재 구간의 최소값과 최대값

            for (int i = 1; i < n; i++) {
                min = Math.min(min, array[i]);
                max = Math.max(max, array[i]);

                // 현재 구간의 최대 점수가 mid보다 크면 새로운 구간 시작
                if (max - min > mid) {
                    groups++; // 구간 개수 증가
                    min = max = array[i]; // 새 구간의 초기값 설정
                }
            }

            // 구간 개수가 m 이하인 경우
            if (groups <= m) {
                result = mid; // 가능한 결과 업데이트
                high = mid - 1; // 더 낮은 최대 점수 찾기
            } else {
                low = mid + 1; // 더 높은 최대 점수 탐색
            }
        }

        System.out.println(result);
    }
}