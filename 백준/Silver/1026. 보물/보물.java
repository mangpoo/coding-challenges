/*
// 바꿔치기
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String A = st.nextToken();
        String B = st.nextToken();

        String minA = A.replace('6', '5');
        String minB = B.replace('6', '5');

        String maxA = A.replace('5', '6');
        String maxB = B.replace('5', '6');

        int minSum = Integer.parseInt(minA) + Integer.parseInt(minB);
        int maxSum = Integer.parseInt(maxA) + Integer.parseInt(maxB);

        System.out.println(minSum + " " + maxSum);
        br.close();
    }
}
*/

// 보물

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int N = Integer.parseInt(br.readLine());

        Integer[] A = new Integer[N];
        Integer[] B = new Integer[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            B[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(A);


        Arrays.sort(B, Collections.reverseOrder());


        int sum = 0;
        for (int i = 0; i < N; i++) {
            sum += A[i] * B[i];
        }
        System.out.println(sum);
        br.close();
    }
}
