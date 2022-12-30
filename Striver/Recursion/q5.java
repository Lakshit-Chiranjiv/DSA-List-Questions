package Striver.Recursion;

public class q5 {
    // program to print all the numbers from 1 to n using recursion backtracking
    public static void main(String[] args) {
        int n = 5;
        print(n, 1);
    }

    static void print(int i, int n) {
        if (i < 1) return;
        print(i - 1, n);
        System.out.print(i + " ");
    }
}
