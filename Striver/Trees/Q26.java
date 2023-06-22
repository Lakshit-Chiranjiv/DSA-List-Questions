package Striver.Trees;

import java.util.*;

public class Q26 {
    // Print all the nodes at distance k from the given node in a binary tree

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

    public List<Integer> distanceK(Node root, Node target, int k) {
        Map<Node, Node> parents = new HashMap<>();
        markParents(root, parents, target);

        Queue<Node> q = new LinkedList<>();
        q.add(target);
        Set<Node> seen = new HashSet<>();
        seen.add(target);
        int dist = 0;
        while (!q.isEmpty()){
            if (dist == k){
                List<Integer> ans = new ArrayList<>();
                for (Node node : q){
                    ans.add(node.data);
                }
                return ans;
            }
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
            dist++;
        }
        return new ArrayList<>();
    }

    public static void main(String[] args) {
        Node root = new Node(3);
        root.left = new Node(5);
        root.right = new Node(1);
        root.left.left = new Node(6);
        root.left.right = new Node(2);
        root.right.left = new Node(0);
        root.right.right = new Node(8);
        root.left.right.left = new Node(7);
        root.left.right.right = new Node(4);

        Q26 ob = new Q26();
        List<Integer> ans = ob.distanceK(root, root.left, 2);
        System.out.println(ans);
    }
}
