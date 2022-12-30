package Striver.Recursion;

public class q6 {
    // program to print all the numbers from n to 1 using recursion backtracking
    public static void main(String[] args) {
        int n = 5;
        print(1, n);
    }

    static void print(int i, int n) {
        if (i > n) return;
        print(i + 1, n);
        System.out.print(i + " ");
    }
}
