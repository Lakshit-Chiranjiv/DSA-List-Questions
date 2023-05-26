package Striver.Trees;

public class Q14{
    // Check if both the trees are identical

    public boolean isIdentical(Node root1, Node root2){
        if(root1 == null && root2 == null) return true;
        if(root1 == null || root2 == null) return false;
        // checking by preorder traversal
        return root1.data == root2.data && isIdentical(root1.left, root2.left) && isIdentical(root1.right, root2.right);
    }

    public static void main(String[] args) {
        Q14 sol = new Q14();
        Node root1 = new Node(1);
        root1.left = new Node(2);
        root1.right = new Node(3);

        Node root2 = new Node(1);
        root2.left = new Node(2);
        root2.right = new Node(3);

        System.out.println(sol.isIdentical(root1, root2));   
    }
}