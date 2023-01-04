package Striver.Recursion;

public class q21 {
        // n-queens problem - storing the queen's position for leftrow, upperleft diagonal and lowerleft diagonal

        public static void main(String[] args) {
            int n = 4;
            int[][] board = new int[n][n];
            boolean[] leftRow = new boolean[n];
            boolean[] upperLeftDiagonal = new boolean[2 * n - 1];
            boolean[] lowerLeftDiagonal = new boolean[2 * n - 1];
            solveNQueens(board, 0, leftRow, upperLeftDiagonal, lowerLeftDiagonal);
        }

        public static void solveNQueens(int[][] board, int col, boolean[] leftRow, boolean[] upperLeftDiagonal, boolean[] lowerLeftDiagonal) {
            if (col == board.length) {
                printBoard(board);
                return;
            }

            for (int i = 0; i < board.length; i++) {
                if (isSafe(board, i, col, leftRow, upperLeftDiagonal, lowerLeftDiagonal)) {
                    board[i][col] = 1;
                    leftRow[i] = true;
                    upperLeftDiagonal[i - col + board.length - 1] = true;
                    lowerLeftDiagonal[i + col] = true;
                    solveNQueens(board, col + 1, leftRow, upperLeftDiagonal, lowerLeftDiagonal);
                    board[i][col] = 0;
                    leftRow[i] = false;
                    upperLeftDiagonal[i - col + board.length - 1] = false;
                    lowerLeftDiagonal[i + col] = false;
                }
            }
        }

        public static boolean isSafe(int[][] board, int row, int col, boolean[] leftRow, boolean[] upperLeftDiagonal, boolean[] lowerLeftDiagonal) {
            if (leftRow[row])
                return false;
            if (upperLeftDiagonal[row - col + board.length - 1])
                return false;
            if (lowerLeftDiagonal[row + col])
                return false;
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