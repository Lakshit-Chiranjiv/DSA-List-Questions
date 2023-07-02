package Striver.Trees;

import java.util.*;

public class Q28{
    // Find total number of nodes in a complete binary tree

    public int countNodes(TreeNode root) {
        if(root == null) return 0;
        int lh = 0, rh = 0;
        TreeNode curr = root;
        while(curr != null){
            lh++;
            curr = curr.left;
        }
        curr = root;
        while(curr != null){
            rh++;
            curr = curr.right;
        }
        if(lh == rh) return (int)Math.pow(2, lh) - 1;
        return 1 + countNodes(root.left) + countNodes(root.right);
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2); root.right = new Node(3);
        root.left.left = new Node(4); root.left.right = new Node(5);
        root.right.left = new Node(6); root.right.right = new Node(7);

        Q28 q = new Q28();
        System.out.println(q.countNodes(root));
    }
}