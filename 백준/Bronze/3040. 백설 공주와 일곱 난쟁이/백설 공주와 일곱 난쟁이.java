import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        int[] numbers = new int[9];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < 9; i++){
            numbers[i] = sc.nextInt();
        }

        Random random = new Random();

        HashSet<Integer> set = new HashSet<>();

        int sum, count;

        while (true) {
            set = new HashSet<>();
            sum = 0;
            count = 0;

            while (count < 7) {
                int index = random.nextInt(numbers.length);
                if (set.add(index)) { // 중복되지 않는 인덱스만 추가
                    sum += numbers[index];
                    count++;
                }
            }

            if (sum == 100) {
                break;
            }
        }
        for (int i : set) {
            System.out.println(numbers[i]);
        }
    }
}