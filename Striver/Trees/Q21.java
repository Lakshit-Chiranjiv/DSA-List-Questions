package Striver.Trees;

public class Q21{
    // Check if binary tree is symmetric or not

    public boolean isSymmetric(Node root) {
        if(root == null) return true;
        return areSymmetricSubtrees(root.left, root.right);
    }

    public boolean areSymmetricSubtrees(Node leftSubTree, Node rightSubTree){
        if(leftSubTree == null || rightSubTree == null) return leftSubTree == rightSubTree;
        if(leftSubTree.data != rightSubTree.data) return false;
        return areSymmetricSubtrees(leftSubTree.left, rightSubTree.right) && areSymmetricSubtrees(leftSubTree.right, rightSubTree.left);
    }

    public static void main(String[] args) {
        Q21 q = new Q21();
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(2);
        System.out.println(q.isSymmetric(root));   
    }
}