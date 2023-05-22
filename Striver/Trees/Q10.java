package Striver.Trees;

public class Q10{
    // Maximum Depth of Binary Tree

    public int maxDepth(Node root) {
        if(root == null) return 0;
        return 1 + Math.max(maxDepth(root.left),maxDepth(root.right));
    }

    public static void main(String[] args) {
        Node root = new Node(3);
        root.left = new Node(9); root.right = new Node(20);
        root.right.left = new Node(15); root.right.right = new Node(7);
        Q10 sol = new Q10();
        
        System.out.println(sol.maxDepth(root));
    }

}