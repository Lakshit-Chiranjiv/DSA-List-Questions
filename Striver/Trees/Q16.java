package Striver.Trees;
import java.util.*;

public class Q16 {
  // boundary traversal of a binary tree - anticlockwise
  
  public static void LeftTraversal(Node root, ArrayList<Integer> ans){
      if(root == null) return;
      if(root.left != null){
          ans.add(root.data);
          LeftTraversal(root.left, ans);
      }
      else if(root.right != null){
          ans.add(root.data);
          LeftTraversal(root.right, ans);
      }
  }

    public static void RightTraversal(Node root, ArrayList<Integer> ans){
        if(root == null) return;
        if(root.right != null){
            RightTraversal(root.right, ans);
            ans.add(root.data);
        }
        else if(root.left != null){
            RightTraversal(root.left, ans);
            ans.add(root.data);
        }
    }

    public static void LeafTraversal(Node root, ArrayList<Integer> ans){
        if(root == null) return;
        LeafTraversal(root.left, ans);
        if(root.left == null && root.right == null) ans.add(root.data);
        LeafTraversal(root.right, ans);
    }

    public static ArrayList <Integer> printBoundary(Node root)
    {
        ArrayList<Integer> ans = new ArrayList<>();
        if(root == null) return ans;
        ans.add(root.data);
        LeftTraversal(root.left, ans);
        LeafTraversal(root, ans);
        RightTraversal(root.right, ans);
        return ans;
    }

    public static void main(String[] args) {
        Node root = new Node(20);
        root.left = new Node(8);
        root.left.left = new Node(4);
        root.left.right = new Node(12);
        root.left.right.left = new Node(10);
        root.left.right.right = new Node(14);
        root.right = new Node(22);
        root.right.right = new Node(25);
        ArrayList<Integer> ans = printBoundary(root);
        for(int i : ans) System.out.print(i + " ");
    }
}
