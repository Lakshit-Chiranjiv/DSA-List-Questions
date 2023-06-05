package Striver.Trees;

import java.util.*;

public class Q22{
    // Print root to node path in binary tree

    public static boolean printPath(Node root, int target, ArrayList<Integer> path){
        if(root == null) return false;
        path.add(root.data);
        if(root.data == target) return true;
        if(printPath(root.left, target, path) || printPath(root.right, target, path)) return true;
        path.remove(path.size() - 1);
        return false;
    }

    public static void main(String[] args) {
        Q22 q = new Q22();
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        ArrayList<Integer> path = new ArrayList<>();
        System.out.println(printPath(root, 3, path));
        System.out.println(path);
    }
}