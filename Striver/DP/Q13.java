package Striver.DP;

import java.util.Arrays;

public class Q13 {
    // Cherry Pickup | 3D DP
    // Alice & Bob are playing a game. They are given a grid of size n x m. Each cell of the grid has a value. Alice and Bob take turns in a way, that in each turn, a player picks two cells and removes them from the grid. The score of each player is the sum of the values of the cells they picked. The player with the maximum score wins. If both players play optimally, what is the maximum possible score that Alice can achieve?
    // alice starts from (0, 0) and bob starts from (0, m - 1)
    // they can only down, left down, right down
    // they can move to the same cell in the next row
    // their target is to maximize the sum of the values of the cells they picked
    // if they land on the same cell, they will only pick it once

    // dp[i][j][k] = max value that can be picked by alice and bob if they start from (i, j) and (i, k)

    // recursive solution - Time: O(3^n) | Space: O(n)
    public static int cherryPickup(int[][] grid, int i, int j1, int j2) {
        int n = grid.length;
        int m = grid[0].length;
        if (j1 < 0 || j1 >= m || j2 < 0 || j2 >= m)
            return Integer.MIN_VALUE;
        if (i == n){
            if(j1 == j2)
                return grid[i][j1];
            return grid[i][j1] + grid[i][j2];
        }
        int ans = 0;
        for(int x = -1; x <= 1; x++){
            for(int y = -1; y <= 1; y++){
                if(j1 == j2)
                    ans = Math.max(ans, cherryPickup(grid, i + 1, j1 + x, j2 + y) + grid[i][j1]);
                else
                    ans = Math.max(ans, cherryPickup(grid, i + 1, j1 + x, j2 + y) + grid[i][j1] + grid[i][j2]);
            }
        }
        return ans;
    }

    // memoization - Time: O(n^3) | Space: O(n^3)
    public static int cherryPickupMem(int[][] grid, int i, int j1, int j2, int[][][] dp) {
        int n = grid.length;
        int m = grid[0].length;
        if (j1 < 0 || j1 >= m || j2 < 0 || j2 >= m)
            return Integer.MIN_VALUE;
        if (i == n){
            if(j1 == j2)
                return grid[i][j1];
            return grid[i][j1] + grid[i][j2];
        }
        if(dp[i][j1][j2] != -1)
            return dp[i][j1][j2];
        int ans = 0;
        for(int x = -1; x <= 1; x++){
            for(int y = -1; y <= 1; y++){
                if(j1 == j2)
                    ans = Math.max(ans, cherryPickup(grid, i + 1, j1 + x, j2 + y) + grid[i][j1]);
                else
                    ans = Math.max(ans, cherryPickup(grid, i + 1, j1 + x, j2 + y) + grid[i][j1] + grid[i][j2]);
            }
        }
        return dp[i][j1][j2] = ans;
    }

    // tabulation - Time: O(n^3) | Space: O(n^3)
    public static int cherryPickupTab(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][][] dp = new int[n][m][m];
        for(int j1 = 0; j1 < m; j1++){
            for(int j2 = 0; j2 < m; j2++){
                if(j1 == j2)
                    dp[n-1][j1][j2] = grid[n-1][j1];
                else
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2];
            }
        }
        for(int i = n - 2; i >= 0; i--){
            for(int j1 = 0; j1 < m; j1++){
                for(int j2 = 0; j2 < m; j2++){
                    int ans = 0;
                    for(int x = -1; x <= 1; x++){
                        for(int y = -1; y <= 1; y++){
                            int val = 0;
                            if(j1 == j2)
                                val = grid[i][j1];
                            else
                                val = grid[i][j1] + grid[i][j2];
                            if(j1 + x >= 0 && j1 + x < m && j2 + y >= 0 && j2 + y < m)
                                val += dp[i+1][j1+x][j2+y];
                            else
                                val += Integer.MIN_VALUE;
                            ans = Math.max(ans, val);
                        }
                    }
                    dp[i][j1][j2] = ans;
                }
            }
        }
        return dp[0][0][m - 1];
    }

    // space optimization - Time: O(n^3) | Space: O(n^2)
    public static int cherryPickupSpOpt(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int[][] dp = new int[m][m];
        int[][] curr = new int[m][m];
        for(int j1 = 0; j1 < m; j1++){
            for(int j2 = 0; j2 < m; j2++){
                if(j1 == j2)
                    dp[j1][j2] = grid[n-1][j1];
                else
                    dp[j1][j2] = grid[n-1][j1] + grid[n-1][j2];
            }
        }
        for(int i = n - 2; i >= 0; i--){
            for(int j1 = 0; j1 < m; j1++){
                for(int j2 = 0; j2 < m; j2++){
                    int ans = 0;
                    for(int x = -1; x <= 1; x++){
                        for(int y = -1; y <= 1; y++){
                            int val = 0;
                            if(j1 == j2)
                                val = grid[i][j1];
                            else
                                val = grid[i][j1] + grid[i][j2];
                            if(j1 + x >= 0 && j1 + x < m && j2 + y >= 0 && j2 + y < m)
                                val += dp[j1+x][j2+y];
                            else
                                val += Integer.MIN_VALUE;
                            ans = Math.max(ans, val);
                        }
                    }
                    curr[j1][j2] = ans;
                }
            }
            dp = curr;
        }
        return dp[0][m - 1];
    }

    public static void main(String[] args) {
        int[][] grid = {{3,1,1},{2,5,1},{1,5,5},{2,1,1}};
        System.out.println(cherryPickup(grid, 0, 0, grid[0].length - 1));
        int[][][] dp = new int[grid.length][grid[0].length][grid[0].length];
        for(int[][] d: dp)
            for(int[] d1: d)
                Arrays.fill(d1, -1);
        System.out.println(cherryPickupMem(grid, 0, 0, grid[0].length - 1, dp));
        System.out.println(cherryPickupTab(grid));
        System.out.println(cherryPickupSpOpt(grid));
    }
}
