package Striver.Trees;
import java.util.*;

class Pair{
    Node node;
    int num;

    Pair(Node node, int num){
        this.node = node;
        this.num = num;
    }
}

public class Q24{
    // Maximum width of a binary tree

    public static int maxWidth(Node root){
        if(root == null) return 0;
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(root, 0));

        int ans = 0;

        while(!q.isEmpty()){
            int size = q.size();
            int min = q.peek().num;
            int start = 0;
            int end = 0;

            for(int i=0; i<size; i++){
                int curr = q.peek().num - min;
                Node temp = q.peek().node;
                q.poll();

                if(i == 0) start = curr;
                if(i == size-1) end = curr;

                if(temp.left != null) q.add(new Pair(temp.left, 2*curr+1));
                if(temp.right != null) q.add(new Pair(temp.right, 2*curr+2));
            }

            ans = Math.max(ans, end-start+1);
        }
        return ans;

    }

    public static void main(String[] args) {
        Node root = new Node(10);
        root.left = new Node(20);
        root.right = new Node(30);
        root.left.left = new Node(40);
        root.left.right = new Node(50);
        root.right.left = new Node(60);
        root.right.right = new Node(70);

        System.out.println(maxWidth(root));
    }

}