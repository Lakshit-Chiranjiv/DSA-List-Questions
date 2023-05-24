package Striver.Trees;

public class Q12{
    // Diameter of a Binary Tree

    public int diameterOfBinaryTree(Node root) {
        if(root == null) return 0;
        int[] ans = new int[1];
        height(root, ans);
        return ans[0];
    }

    public int height(Node root, int[] ans){
        if(root == null) return 0;
        int left = height(root.left, ans);
        int right = height(root.right, ans);
        ans[0] = Math.max(ans[0], left + right);
        return Math.max(left, right) + 1;
    }

    public static void main(String[] args) {
        Q12 sol = new Q12();
        Node root = new Node(1);
        root.left = new Node(2);
        root.left.left = new Node(4);
        root.right = new Node(3);
        System.out.println(sol.diameterOfBinaryTree(root));   
    }
}