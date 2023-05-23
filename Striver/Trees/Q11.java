package Striver.Trees;

public class Q11{
    // Check if a binary tree is balanced or not

    public boolean isBalanced(Node root) {
        if(root == null) return true;
        return height(root) != -1;
    }

    public int height(Node root){
        if(root == null) return 0;
        int left = height(root.left);
        if(left == -1) return -1;
        int right = height(root.right);
        if(right == -1) return -1;
        if(Math.abs(left - right) > 1) return -1;
        return Math.max(left, right) + 1;
    }

    public static void main(String[] args) {
        Node root = new Node(10);
        root.left = new Node(20);
        root.left.left = new Node(40);
        root.left.right = new Node(50);
        root.right = new Node(30);
        root.right.right = new Node(70);
        root.right.right.right = new Node(80);
        Q11 q = new Q11();
        
        System.out.println(q.isBalanced(root));
    }
}