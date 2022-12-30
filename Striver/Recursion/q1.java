package Striver.Recursion;

// program to print all the numbers from 1 to n using recursion

import java.util.*;
class q1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        print(1,n);
    }

    static void print(int i, int n) {
        if(i>n) return;
        System.out.print(i+" ");
        print(i+1,n);
    }
}