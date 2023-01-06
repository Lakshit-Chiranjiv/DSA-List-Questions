package Striver.Recursion;

import java.util.ArrayList;
import java.util.List;

public class q25 {
    //rat in a maze problem - print all paths in lexicographical order
    // Up - U, Down - D, Left - L, Right - R
    // 1 - path is open, 0 - path is blocked
    // visit each cell only once
    // start from (0,0) and end at (n-1,m-1)

    public static void main(String[] args) {
        int[][] maze = {
                {1, 0, 0, 0},
                {1, 1, 0, 1},
                {1, 1, 0, 0},
                {0, 1, 1, 1}
        };
        int m = maze.length;
        int n = maze[0].length;
        String path = "";
        List<String> paths = new ArrayList<>();
        int [][] visited = new int[m][n];
        int[] idir = {1, 0, 0, -1};
        int[] jdir = {0, -1, 1, 0};
        String[] dir = {"D", "L", "R", "U"};
        ratInMaze(maze, 0, 0, m, n, path, paths, visited, idir, jdir, dir);

        ratInMaze(maze, 0, 0, m, n, path, paths, visited);
    }

    public static void ratInMaze(int[][] maze, int i, int j, int m, int n, String path, List<String> paths, int[][] visited) {
        if (i < 0 || j < 0 || i >= m || j >= n || maze[i][j] == 0 || visited[i][j] == 1) {
            return;
        }
        if (i == m - 1 && j == n - 1) {
            paths.add(path);
            return;
        }
        visited[i][j] = 1;
        ratInMaze(maze, i + 1, j, m, n, path + "D", paths, visited);
        ratInMaze(maze, i, j - 1, m, n, path + "L", paths, visited);
        ratInMaze(maze, i, j + 1, m, n, path + "R", paths, visited);
        ratInMaze(maze, i - 1, j, m, n, path + "U", paths, visited);
        visited[i][j] = 0;
    }

    public static void ratInMaze(int[][] maze, int i, int j, int m, int n, String path, List<String> paths, int[][] visited, int[] idir, int[] jdir, String[] dir) {
        if (i < 0 || j < 0 || i >= m || j >= n || maze[i][j] == 0 || visited[i][j] == 1) {
            return;
        }
        if (i == m - 1 && j == n - 1) {
            paths.add(path);
            return;
        }
        visited[i][j] = 1;
        for (int d = 0; d < 4; d++) {
            ratInMaze(maze, i + idir[d], j + jdir[d], m, n, path + dir[d], paths, visited, idir, jdir, dir);
        }
        visited[i][j] = 0;
    }



}