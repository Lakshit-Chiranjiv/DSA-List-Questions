package Striver.Recursion;

class q20 {
    // n-queens problem - backtracking

    public static void main(String[] args) {
        int n = 4;
        int[][] board = new int[n][n];
        solveNQueens(board, 0);
    }

    public static void solveNQueens(int[][] board, int col) {
        if (col == board.length) {
            printBoard(board);
            return;
        }

        for (int i = 0; i < board.length; i++) {
            if (isSafe(board, i, col)) {
                board[i][col] = 1;
                solveNQueens(board, col + 1);
                board[i][col] = 0;
            }
        }
    } 

    public static boolean isSafe(int[][] board, int row, int col) {

        // checking for left side same row
        int i = row, j = col;
        while (j >= 0) {
            if (board[i][j] == 1)
                return false;
            j--;
        }

        // checking for upper left diagonal
        i = row;
        j = col;
        while (i >= 0 && j >= 0) {
            if (board[i][j] == 1)
                return false;
            i--;
            j--;
        }

        //checking for lower left diagonal
        i = row;
        j = col;
        while (i < board.length && j >= 0) {
            if (board[i][j] == 1)
                return false;
            i++;
            j--;
        }

        return true;
    }

    public static void printBoard(int[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}