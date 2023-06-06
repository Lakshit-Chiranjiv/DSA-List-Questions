package Striver.Trees;

public class Q23{
    // Lowest Common Ancestor of a Binary Tree

    public Node lowestCommonAncestor(Node root, Node p, Node q) {
        if(root == null || root == p || root == q) return root;
        
        Node left = lowestCommonAncestor(root.left, p, q);
        Node right = lowestCommonAncestor(root.right, p, q);
        
        if(left == null) return right;
        if(right == null) return left;

        return root;
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

        Q23 q = new Q23();
        Node ans = q.lowestCommonAncestor(root, root.left, root.right);
        System.out.println(ans.data);
    }
}