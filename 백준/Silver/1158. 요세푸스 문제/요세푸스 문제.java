import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;
import java.util.Queue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        LinkedList<Integer> person = new LinkedList<>();
        Queue<Integer> result = new LinkedList<>();

        for (int i = 1; i <= N; i++) {
            person.add(i);
        }

        int index = 0;
        while (!person.isEmpty()) {
            index = (index + K - 1) % person.size();
            result.offer(person.remove(index));
        }

        System.out.print("<");
        while (!result.isEmpty()) {
            System.out.print(result.poll());
            if (!result.isEmpty()) {
                System.out.print(", ");
            }
        }
        System.out.println(">");
    }
}