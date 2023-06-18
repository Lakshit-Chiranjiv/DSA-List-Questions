package Striver.Trees;

import java.util.*;

public class Q25{
    // Implement Child Sum Property in a Binary Tree by incrementing value of nodes

    public static void ChildrenSumProperty(Node root){
        if (root == null) return;
        int child = 0;

        if (root.left != null) child += root.left.data;
        if (root.right != null) child += root.right.data;

        if (child > root.data) root.data = child;
        else {
            if (root.left != null) root.left.data = root.data;
            else if (root.right != null) root.right.data = root.data;
        }

        ChildrenSumProperty(root.left);
        ChildrenSumProperty(root.right);

        int total = 0;
        if (root.left != null) total += root.left.data;
        if (root.right != null) total += root.right.data;

        if (root.left != null || root.right != null) root.data = total;
    }

    public static void main(String[] args) {
        Node root = new Node(50);
        root.left = new Node(7);
        root.right = new Node(2);
        root.left.left = new Node(3);
        root.left.right = new Node(5);
        root.right.left = new Node(1);
        root.right.right = new Node(30);

        ChildrenSumProperty(root);

        Queue<Node> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()){
            Node curr = q.poll();
            System.out.print(curr.data + " ");
            if (curr.left != null) q.add(curr.left);
            if (curr.right != null) q.add(curr.right);
        }
    }
}