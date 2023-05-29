package Striver.Trees;
import java.util.*;
// vertical order traversal of a binary tree

class Tuple{
    Node node;
    int row;
    int col;
    Tuple(Node node, int row, int col){
        this.node = node;
        this.row = row;
        this.col = col;
    }
}

public class Q17 {
    public List<List<Integer>> verticalTraversal(Node root) {
        List<List<Integer>> ans = new ArrayList<>();
        if(root == null) return ans;
        Map<Integer, List<Integer>> map = new HashMap<>();
        Queue<Tuple> q = new LinkedList<>();
        q.add(new Tuple(root, 0, 0));
        int min = 0, max = 0;
        while(!q.isEmpty()){
            Tuple t = q.poll();
            Node node = t.node;
            int row = t.row;
            int col = t.col;
            if(!map.containsKey(col)){
                map.put(col, new ArrayList<>());
            }
            map.get(col).add(node.data);
            if(node.left != null){
                q.add(new Tuple(node.left, row+1, col-1));
                min = Math.min(min, col-1);
            }
            if(node.right != null){
                q.add(new Tuple(node.right, row+1, col+1));
                max = Math.max(max, col+1);
            }
        }
        for(int i=min; i<=max; i++){
            ans.add(map.get(i));
        }
        return ans;
    }

    public static void main(String[] args) {
        Q17 q = new Q17();
        Node root = new Node(3);
        root.left = new Node(9);
        root.right = new Node(20);
        root.right.right = new Node(7);
        root.right.left = new Node(15);
        System.out.println(q.verticalTraversal(root));   
    }
}
