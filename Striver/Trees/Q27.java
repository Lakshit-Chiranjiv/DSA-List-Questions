package Striver.Trees;

import java.util.*;

public class Q27 {
    // Time taken to burn entire binary tree

    public void markParents(Node root, Map<Node, Node> parents, Node target){
        Queue<Node> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()){
            Node curr = q.poll();
            if (curr.left != null){
                parents.put(curr.left, curr);
                q.add(curr.left);
            }
            if (curr.right != null){
                parents.put(curr.right, curr);
                q.add(curr.right);
            }
        }
    }

    public int timeToBurn(Node root, Node target){
        Map<Node, Node> parents = new HashMap<>();
        markParents(root, parents, target);

        Queue<Node> q = new LinkedList<>();
        q.add(target);
        Set<Node> seen = new HashSet<>();
        seen.add(target);
        int time = 0;
        while (!q.isEmpty()){
            int size = q.size();
            for (int i = 0; i < size; i++){
                Node curr = q.poll();
                if (curr.left != null && !seen.contains(curr.left)){
                    seen.add(curr.left);
                    q.add(curr.left);
                }
                if (curr.right != null && !seen.contains(curr.right)){
                    seen.add(curr.right);
                    q.add(curr.right);
                }
                Node parent = parents.get(curr);
                if (parent != null && !seen.contains(parent)){
                    seen.add(parent);
                    q.add(parent);
                }
            }
            time++;
        }
        return time;
    }

    public static void main(String[] args) {
        Q27 q = new Q27();
        Node root = new Node(1);
        root.left = new Node(2);
        root.left.left = new Node(4);
        Node target = root.left.left;
        root.left.right = new Node(5);
        root.left.right.right = new Node(8);
        root.left.right.right.right = new Node(9);
        root.left.right.right.right.left = new Node(10);
        root.left.right.right.right.left.left = new Node(11);
        root.left.right.right.right.left.left.left = new Node(12);
        root.left.right.right.right.left.left.left.left = new Node(13);
        root.left.right.right.right.left.left.left.left.left = new Node(14);
        root.left.right.right.right.left.left.left.left.left.left = new Node(15);
        root.right = new Node(3);
        root.right.right = new Node(7);
        root.right.left = new Node(6);
        System.out.println(q.timeToBurn(root, target));
    }
}
