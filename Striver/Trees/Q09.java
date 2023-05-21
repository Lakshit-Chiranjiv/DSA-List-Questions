package Striver.Trees;
import java.util.*;

public class Q09{
    // Preorder, Inorder, Postorder Traversal in a single iteration using a single stack

    public void preInPost(Node root){
        Stack<Pair> st = new Stack<>();
        st.push(new Pair(root, 1));

        List<Integer> pre = new ArrayList<>();
        List<Integer> in = new ArrayList<>();
        List<Integer> post = new ArrayList<>();

        if(root == null) return;

        while(!st.isEmpty()){
            Pair top = st.peek();
            if(top.state == 1){
                pre.add(top.node.data);
                top.state++;
                if(top.node.left != null){
                    st.push(new Pair(top.node.left, 1));
                }
            }else if(top.state == 2){
                in.add(top.node.data);
                top.state++;
                if(top.node.right != null){
                    st.push(new Pair(top.node.right, 1));
                }
            }else{
                post.add(top.node.data);
                st.pop();
            }
        }

        System.out.println("Preorder: " + pre);
        System.out.println("Inorder: " + in);
        System.out.println("Postorder: " + post);
    }

    public static void main(String[] args) {
        Node root = new Node(10);
        root.left = new Node(20);
        root.left.left = new Node(40);
        root.left.right = new Node(50);
        root.right = new Node(30);
        root.right.left = new Node(60);
        root.right.right = new Node(70);
        
        Q09 q = new Q09();
        q.preInPost(root);
    }
}