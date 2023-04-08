package Striver.DP;

import java.util.*;

public class Q55{
    // Maximum Rectangle Area with all 1's
    public int largestRectangleArea(int[] heights) {
        Stack<Integer> st = new Stack<>();
        int mxa = 0;
        int n = heights.length;

        for (int i = 0; i <= n; i++) {
            while (!st.isEmpty() && (i == n || heights[st.peek()] >= heights[i])) {
                int ht = heights[st.pop()];
                int wd = 0;
                if (st.isEmpty()) {
                    wd = i;
                } else {
                    wd = i - st.peek() - 1;
                }
                mxa = Math.max(mxa, wd * ht);
            }
            st.push(i);
        }
        return mxa;
    }

    public int maximalRectangle(char[][] matrix) {
        int mxa = 0;
        int n = matrix.length;
        if (n == 0)
            return 0;
        int m = matrix[0].length;
        int[] heights = new int[m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == '0') {
                    heights[j] = 0;
                } else {
                    heights[j] += 1;
                }
            }
            mxa = Math.max(mxa, largestRectangleArea(heights));
        }
        return mxa;
    }
    
}