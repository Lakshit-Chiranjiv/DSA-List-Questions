package Striver.Trees;
import java.util.*;

public class Q07{
    // Iterative Postorder Traversal using 2 stacks

    public static List<Integer> postorderTraversal(Node root){
        List<Integer> ans = new ArrayList<>();
        if(root == null) return ans;

        Stack<Node> s1 = new Stack<>();
        Stack<Node> s2 = new Stack<>();

        s1.push(root);
        while(!s1.isEmpty()){
            Node curr = s1.pop();
            s2.push(curr);

            if(curr.left != null) s1.push(curr.left);
            if(curr.right != null) s1.push(curr.right);
        }

        while(!s2.isEmpty()){
            ans.add(s2.pop().data);
        }

        return ans;
    }

    public static void main(String[] args){
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);

        System.out.println(postorderTraversal(root));
    }
}