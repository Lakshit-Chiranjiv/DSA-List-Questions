package Striver.Trees;

import java.util.*;

public class Q15{
    // ZigZag traversal of a binary tree

    public List<List<Integer>> zigzagLevelOrder(Node root) {
        List<List<Integer>> ans = new ArrayList<>();
        if(root == null)return ans;
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        boolean flag = true;
        while(!q.isEmpty()){
            int size = q.size();
            List<Integer> temp = new ArrayList<>();
            while(size-- > 0){
                Node curr = q.poll();
                temp.add(curr.data);
                if(curr.left != null)q.add(curr.left);
                if(curr.right != null)q.add(curr.right);
            }
            if(flag){
                ans.add(temp);
                flag = false;
            }else{
                Collections.reverse(temp);
                ans.add(temp);
                flag = true;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        Node root = new Node(3);
        root.left = new Node(9);root.right = new Node(20);
        root.right.left = new Node(15);root.right.right = new Node(7);
        Q15 q = new Q15();
        List<List<Integer>> ans = q.zigzagLevelOrder(root);
        for(List<Integer> i : ans){
            for(int j : i){
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }

}