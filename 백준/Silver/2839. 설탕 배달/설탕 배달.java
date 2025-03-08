// 설탕 배달

import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int result = -1;

        for (int i = n / 5; i >= 0; i--) {
            int count = n - (5 * i);
            if (count % 3 == 0) {
                result = i + count / 3;
                break;
            }
        }

        System.out.println(result);
    }
}