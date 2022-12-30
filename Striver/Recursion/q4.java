package Striver.Recursion;

public class q4 {
    // program to print sum of all the numbers from 1 to n using recursion by returning sum
    public static void main(String[] args) {
        int n = 5;
        System.out.println(sum(n));
    }

    static int sum(int i) {
        if (i < 1) return 0;
        return i + sum(i - 1);
    }
}
