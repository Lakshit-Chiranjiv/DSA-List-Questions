package Striver.DP;

public class Q52 {
    // evaluate boolean expression to true

    // recursive solution - Time: O(3^n) Space: O(n)
    public int countWays(String s, int i, int j, boolean isTrue) {
        if(i > j) return 0;
        if(i == j){
            if(isTrue) return s.charAt(i) == 'T' ? 1 : 0;
            else return s.charAt(i) == 'F' ? 1 : 0;
        }

        int ans = 0;
        for(int k = i+1; k <= j-1; k+=2){
            int lt = countWays(s, i, k-1, true);
            int lf = countWays(s, i, k-1, false);
            int rt = countWays(s, k+1, j, true);
            int rf = countWays(s, k+1, j, false);

            if(s.charAt(k) == '&'){
                if(isTrue) ans += lt * rt;
                else ans += lt * rf + lf * rt + lf * rf;
            }
            else if(s.charAt(k) == '|'){
                if(isTrue) ans += lt * rt + lt * rf + lf * rt;
                else ans += lf * rf;
            }
            else if(s.charAt(k) == '^'){
                if(isTrue) ans += lt * rf + lf * rt;
                else ans += lt * rt + lf * rf;
            }
        }

        return ans;
    }

    // memoization - Time: O(n^3) Space: O(n^2)
    public int countWaysMemo(String s, int i, int j, boolean isTrue, int[][][] dp) {
        if(i > j) return 0;
        if(i == j){
            if(isTrue) return s.charAt(i) == 'T' ? 1 : 0;
            else return s.charAt(i) == 'F' ? 1 : 0;
        }
        if(dp[i][j][isTrue ? 1 : 0] != -1) return dp[i][j][isTrue ? 1 : 0];

        int ans = 0;
        for(int k = i+1; k <= j-1; k+=2){
            int lt = countWaysMemo(s, i, k-1, true, dp);
            int lf = countWaysMemo(s, i, k-1, false, dp);
            int rt = countWaysMemo(s, k+1, j, true, dp);
            int rf = countWaysMemo(s, k+1, j, false, dp);

            if(s.charAt(k) == '&'){
                if(isTrue) ans += lt * rt;
                else ans += lt * rf + lf * rt + lf * rf;
            }
            else if(s.charAt(k) == '|'){
                if(isTrue) ans += lt * rt + lt * rf + lf * rt;
                else ans += lf * rf;
            }
            else if(s.charAt(k) == '^'){
                if(isTrue) ans += lt * rf + lf * rt;
                else ans += lt * rt + lf * rf;
            }
        }

        return dp[i][j][isTrue ? 1 : 0] = ans;
    }

    // tabulation - Time: O(n^3) Space: O(n^2)
    public int countWaysTab(String s, int n) {
        int[][][] dp = new int[n][n][2];
        for(int i = n-1; i >= 0; i--){
            for(int j = i; j < n; j++){
                if(i == j){
                    if(s.charAt(i) == 'T') dp[i][j][1] = 1;
                    else dp[i][j][0] = 1;
                }
            }
        }

        for(int gap = 2; gap < n; gap+=2){
            for(int i = 0; i < n-gap; i+=2){
                int j = i + gap;
                for(int k = i+1; k <= j-1; k+=2){
                    if(s.charAt(k) == '&'){
                        dp[i][j][1] += dp[i][k-1][1] * dp[k+1][j][1];
                        dp[i][j][0] += dp[i][k-1][0] * dp[k+1][j][0] + dp[i][k-1][1] * dp[k+1][j][0] + dp[i][k-1][0] * dp[k+1][j][1];
                    }
                    else if(s.charAt(k) == '|'){
                        dp[i][j][1] += dp[i][k-1][1] * dp[k+1][j][1] + dp[i][k-1][1] * dp[k+1][j][0] + dp[i][k-1][0] * dp[k+1][j][1];
                        dp[i][j][0] += dp[i][k-1][0] * dp[k+1][j][0];
                    }
                    else if(s.charAt(k) == '^'){
                        dp[i][j][1] += dp[i][k-1][1] * dp[k+1][j][0] + dp[i][k-1][0] * dp[k+1][j][1];
                        dp[i][j][0] += dp[i][k-1][1] * dp[k+1][j][1] + dp[i][k-1][0] * dp[k+1][j][0];
                    }
                }
            }
        }

        return dp[0][n-1][1];

    }

    public static void main(String[] args) {
        Q52 obj = new Q52();
        String s = "T|T&F^T";
        int n = s.length();
        int[][][] dp = new int[n][n][2];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                for(int k = 0; k < 2; k++){
                    dp[i][j][k] = -1;
                }
            }
        }
        System.out.println(obj.countWays(s, 0, n-1, true));
        System.out.println(obj.countWaysMemo(s, 0, n-1, true, dp));
        System.out.println(obj.countWaysTab(s, n));
    }
}
