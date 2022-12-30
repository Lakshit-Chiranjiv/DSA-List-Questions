package Striver.Recursion;

public class q2 {
    // program to print all the numbers from n to 1 using recursion
    public static void main(String[] args) {
        int n = 5;
        print(n, n);
    }

    static void print(int i, int n) {
        if (i < 1) return;
        System.out.print(i + " ");
        print(i - 1, n);
    }
}
