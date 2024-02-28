import java.util.HashSet;
import java.util.Random;
import java.util.Set;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        int[] numbers = new int[9];
        Scanner sc = new Scanner(System.in);
        for(int i = 0; i < 9; i++){
            System.out.print("");
            numbers[i] = sc.nextInt();
        }
        
        Random random = new Random();
        
        Set<Integer> selectedIndexes;
        
        int sum, count;

        while (true) {
            selectedIndexes = new HashSet<>();
            sum = 0;
            count = 0;

            while (count < 7) {
                int index = random.nextInt(numbers.length);
                if (selectedIndexes.add(index)) { // 중복되지 않는 인덱스만 추가
                    sum += numbers[index];
                    count++;
                }
            }

            if (sum == 100) {
                break; // 합이 100이 되는 조합을 찾았으면 루프 탈출
            }
        }

        // 조합 출력
        for (int index : selectedIndexes) {
            System.out.println(numbers[index]);
        }
    }
}