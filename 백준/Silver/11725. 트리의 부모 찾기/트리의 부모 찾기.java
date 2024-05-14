import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<List<Integer>> list = new ArrayList<>();
        for(int i = 0; i <= n; i++){
            list.add(new ArrayList<>());
        }
        // 트리 값 받기
        for(int i = 1; i < n; i++){
            int l = sc.nextInt();
            int r = sc.nextInt();
            list.get(l).add(r);
            list.get(r).add(l);
        }
        int[] parent = new int[n + 1];
        boolean[] v = new boolean[n + 1];
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        v[1] = true;

        while(!q.isEmpty()){
            int node = q.poll();
            for(int i : list.get(node)){
                if(!v[i]){
                    parent[i] = node;
                    v[i] = true;
                    q.add(i);
                }
            }
        }
        // 2번 노드부터 부모 노드 출력
        for (int i = 2; i <= n; i++) {
            System.out.println(parent[i]);
        }
    }
}