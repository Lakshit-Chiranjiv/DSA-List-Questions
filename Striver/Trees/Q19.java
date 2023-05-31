package Striver.Trees;

import java.util.*;

class Pair{
    Node node;
    int col;
    Pair(Node node, int col){
        this.node = node;
        this.col = col;
    }
}

public class Q19{
    // Bottom view of a binary tree
    public List<Integer> bottomView(Node root){
        List<Integer> ans = new ArrayList<>();
        if(root == null) return ans;
        Map<Integer, Integer> map = new HashMap<>();
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(root, 0));
        int min = 0, max = 0;
        while(!q.isEmpty()){
            Pair p = q.poll();
            Node node = p.node;
            int col = p.col;
            map.put(col, node.data);
            if(node.left != null){
                q.add(new Pair(node.left, col-1));
                min = Math.min(min, col-1);
            }
            if(node.right != null){
                q.add(new Pair(node.right, col+1));
                max = Math.max(max, col+1);
            }
        }
        for(int i=min; i<=max; i++){
            ans.add(map.get(i));
        }
        return ans;
    }

    public static void main(String[] args) {
        Q19 q = new Q19();
        Node root = new Node(3);
        root.left = new Node(9);
        root.right = new Node(20);
        root.right.right = new Node(7);
        root.right.left = new Node(15);
        System.out.println(q.bottomView(root));
    }
}