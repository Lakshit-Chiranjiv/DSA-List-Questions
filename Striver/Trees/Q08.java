package Striver.Trees;
import java.util.*;

public class Q08 {
    // Iterative Postorder Traversal using 1 Stack

    public static List<Integer> postorderTraversal1(Node root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) return ans;

        Stack<Node> st = new Stack<>();
        st.push(root);

        while (!st.isEmpty()) {
            Node curr = st.pop();
            ans.add(curr.data);

            if (curr.left != null) st.push(curr.left);
            if (curr.right != null) st.push(curr.right);
        }

        Collections.reverse(ans);
        return ans;
    }

    public static List<Integer> postorderTraversal2(Node root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) return ans;

        Stack<Node> st = new Stack<>();
        st.push(root);
        Node curr = root;

        while (curr != null || !st.isEmpty()) {
            if (curr != null) {
                st.push(curr);
                curr = curr.left;
            }
            else{
                Node temp = st.peek().right;
                if (temp == null) {
                    temp = st.pop();
                    ans.add(temp.data);

                    while (!st.isEmpty() && temp == st.peek().right) {
                        temp = st.pop();
                        ans.add(temp.data);
                    }
                }
                else curr = temp;
            }
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

        System.out.println(postorderTraversal1(root));
        System.out.println(postorderTraversal2(root));
    }
}
