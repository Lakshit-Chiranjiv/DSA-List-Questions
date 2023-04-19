package Striver.Trees;

import java.util.*;

public class Q06{
    // Iterative Inorder Traversal using Stack

    public static List<Integer> inorderTraversal(Node root){
        List<Integer> ans = new ArrayList<>();
        Stack<Node> stack = new Stack<>();
        Node curr = root;

        while(curr != null || !stack.isEmpty()){
            while(curr != null){
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            ans.add(curr.data);
            curr = curr.right;
        }
        return ans;
    }

    public static void main(String[] args) {
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);

        System.out.println(inorderTraversal(root));
    }

}