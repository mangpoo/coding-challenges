import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String numA = st.nextToken();
        String numB = st.nextToken();

        String minA = numA.replace('6', '5');
        String minB = numB.replace('6', '5');

        String maxA = numA.replace('5', '6');
        String maxB = numB.replace('5', '6');

        int minSum = Integer.parseInt(minA) + Integer.parseInt(minB);
        int maxSum = Integer.parseInt(maxA) + Integer.parseInt(maxB);

        System.out.println(minSum + " " + maxSum);
        br.close();
    }
}
