
import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        Queue<Character> queue = new LinkedList<>();
        String korea = "KOREA";
        int result = 0;

        for(int i = 0; i < korea.length(); i++){
            queue.offer(korea.charAt(i));
        }
        char korea_text = queue.poll();
        for(int i = 0; i < S.length(); i++){
            if(S.charAt(i) == korea_text){
                result += 1;
                queue.offer(korea_text);
                korea_text = queue.poll();
            }
        }

        System.out.println(result);
    }
}
