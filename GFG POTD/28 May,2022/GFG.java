// Shortest Path between Cities
public class GFG { 
    int shortestPath( int x, int y){ 
        // code here
        int c = 0;
        while(x!=y){
            if(x > y)
                x = x/2;
            else
                y = y/2;
            c++;
        }
        return c;
    }
}
