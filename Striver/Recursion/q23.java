package Striver.Recursion;

public class q23 {
    // m - colouring graph problem
    // m = number of colours
    // n = number of vertices
    // graph[][] = adjacency matrix
    // all adjacent vertices should have different colours
    // return true if graph can be coloured with m colours else false

    public static void main(String[] args) {
        int[][] graph = {
                {0, 1, 1, 1},
                {1, 0, 1, 0},
                {1, 1, 0, 1},
                {1, 0, 1, 0}
        };
        int m = 3;
        int n = 4;
        int[] colors = new int[n];
        for (int i = 0; i < n; i++) {
            colors[i] = 0;
        }
        if (solveMColoring(graph, m, n, colors, 0)) {
            System.out.println("Graph can be coloured with " + m + " colours");
        } else {
            System.out.println("Graph cannot be coloured with " + m + " colours");
        }
    }

    public static boolean solveMColoring(int[][] graph, int m, int n, int[] colors, int v) {
        if (v == n) {
            return true;
        }
        for (int i = 1; i <= m; i++) {
            if (isSafe(graph, m, n, colors, v, i)) {
                colors[v] = i;
                if (solveMColoring(graph, m, n, colors, v + 1)) {
                    return true;
                }
                colors[v] = 0;
            }
        }
        return false;
    }

    public static boolean isSafe(int[][] graph, int m, int n, int[] colors, int v, int c) {
        for (int i = 0; i < n; i++) {
            if (graph[v][i] == 1 && colors[i] == c) {
                return false;
            }
        }
        return true;
    }
}
