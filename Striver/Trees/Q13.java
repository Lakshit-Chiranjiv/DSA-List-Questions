package Striver.Trees;

public class Q13{
    // max path sum from any node to any node

    public int maxPathSum(Node root) {
        int[] max = new int[1];
        max[0] = Integer.MIN_VALUE;
        maxPathSum(root, max);
        return max[0];
    }

    public int maxPathSum(Node root, int[] max){
        if(root == null) return 0;
        int left = maxPathSum(root.left, max);
        int right = maxPathSum(root.right, max);
        int max_single = Math.max(Math.max(left, right) + root.data, root.data);
        int max_top = Math.max(max_single, left + right + root.data);
        max[0] = Math.max(max[0], max_top);
        return max_single;
    }

    public static void main(String[] args) {
        Q13 sol = new Q13();
        Node root = new Node(10);
        root.left = new Node(2);
        root.right = new Node(10);
        root.left.left = new Node(20);
        root.left.right = new Node(1);
        root.right.right = new Node(-25);
        root.right.right.left = new Node(3);
        root.right.right.right = new Node(4);
        System.out.println(sol.maxPathSum(root));   
    }

}