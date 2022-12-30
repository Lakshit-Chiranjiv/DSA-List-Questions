package Striver.Recursion;

public class q3 {
    // program to print sum of all the numbers from 1 to n using recursion
    public static void main(String[] args) {
        int n = 5;
        sum(n, 0);
    }

    static void sum(int i, int sum) {
        if (i < 1) {
            System.out.println(sum);
            return;
        }
        sum += i;
        sum(i - 1, sum);
    }
}
