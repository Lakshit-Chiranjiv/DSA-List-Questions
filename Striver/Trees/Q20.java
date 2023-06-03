package Striver.Trees;

import java.util.*;

public class Q20 {
    // right and left view of a binary tree

    // right view
    public void rightView(Node root, int level, List<Integer> ans){
        if(root == null) return;
        if(level == ans.size()){
            ans.add(root.data);
        }
        rightView(root.right, level+1, ans);
        rightView(root.left, level+1, ans);
    }

    // left view
    public void leftView(Node root, int level, List<Integer> ans){
        if(root == null) return;
        if(level == ans.size()){
            ans.add(root.data);
        }
        leftView(root.left, level+1, ans);
        leftView(root.right, level+1, ans);
    }

    public static void main(String[] args) {
        Q20 q = new Q20();
        Node root = new Node(3);
        root.left = new Node(9);
        root.right = new Node(20);
        root.right.right = new Node(7);
        root.right.left = new Node(15);
        List<Integer> ans = new ArrayList<>();
        q.rightView(root, 0, ans);
        System.out.println(ans);
        ans = new ArrayList<>();
        q.leftView(root, 0, ans);
        System.out.println(ans);
    }
}
