
import java.util.Scanner;
import java.util.Arrays;

public class Main{
    public static void main(String[] args){
        String[] ex = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
        Scanner sc = new Scanner(System.in);
        String line = sc.nextLine();
        String[] arr = line.split("");

        int sum = 0;
        int index = 0;

        for (int i = 0; i < arr.length; i++) {
            int new_index = Arrays.asList(ex).indexOf(arr[i]);
            int right = Math.abs(new_index - index);
            int left = ex.length - right;
            if(right < left){
                sum += right;
            }
            else{
                sum += left;
            }
            index = new_index;
        }

        System.out.println(sum);
    }
}