import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        int k = sc.nextInt();
        List<Integer> result = sort(arr, n, k);
        for (Integer num : result) {
            System.out.print(num + " ");
        }
    }

    public static List<Integer> sort(int[] arr, int n, int k){
        List<Integer> result = new ArrayList<>();
        for(int i = 0; i < n; i += n/k){ // n/k 개의 요소를 한 그룹으로 처리
            List<Integer> test = new ArrayList<>();
            for(int j = i; j < i + n/k; j++){ // 현재 그룹의 범위 내에서 요소 추가
                test.add(arr[j]);
            }
            Collections.sort(test);
            result.addAll(test);
        }
        return result;
    }
}