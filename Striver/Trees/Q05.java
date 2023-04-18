package Striver.Trees;
import java.util.*;

public class Q05{
    // Iterative Preorder Traversal of Binary Tree using Stack

    public static List<Integer> preorderTraversal(Node root) {
        List<Integer> list = new ArrayList<>();
        if(root == null) return list;

        Stack<Node> stack = new Stack<>();
        stack.push(root);

        while(!stack.isEmpty()){
            Node curr = stack.pop();
            list.add(curr.data);

            if(curr.right != null) stack.push(curr.right);
            if(curr.left != null) stack.push(curr.left);
        }

        return list;
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);

        System.out.println(preorderTraversal(root));

    }
}