// 두 포인터 이용해서 하기 시간복잡도 O(n)
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            int[] arr = new int[n];
            for (int j = 0; j < n; j++) {
                arr[j] = sc.nextInt();
            }

            int count = twopointer(arr, m);
            System.out.printf("Case #%d: %d\n", i + 1, count);
        }

        sc.close();
    }
    static int twopointer(int[] arr, int m) {
        int left = 0;
        int right = arr.length - 1;
        int count = 0;

        while (left < right) {
            int sum = arr[left] + arr[right];
            if (sum == m) {
                count++;
                left++;
                right--;
            }
            else if (sum < m) {
                left++;
            }
            else {
                right--;
            }
        }

        return count;
    }
}