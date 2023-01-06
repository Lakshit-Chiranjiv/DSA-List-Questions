#rat in a maze problem - print all paths in lexicographical order
# Up - U, Down - D, Left - L, Right - R
# 1 - path is open, 0 - path is blocked
# visit each cell only once
# start from (0,0) and end at (n-1,m-1)

def ratInMaze(maze,i,j,m,n,path,paths,visited):
    if i==m-1 and j==n-1:
        paths.append(path)
        return
    if i<0 or i>=m or j<0 or j>=n or maze[i][j]==0 or visited[i][j]==True:
        return
    visited[i][j]=True
    ratInMaze(maze,i+1,j,m,n,path+'D',paths,visited)
    ratInMaze(maze,i,j-1,m,n,path+'L',paths,visited)
    ratInMaze(maze,i,j+1,m,n,path+'R',paths,visited)
    ratInMaze(maze,i-1,j,m,n,path+'U',paths,visited)
    visited[i][j]=False

def ratInMaze2(maze,i,j,m,n,path,paths,visited,idir,jdir,dir):
    if i==m-1 and j==n-1:
        paths.append(path)
        return
    if i<0 or i>=m or j<0 or j>=n or maze[i][j]==0 or visited[i][j]==True:
        return
    visited[i][j]=True
    for k in range(4):
        ratInMaze2(maze,i+idir[k],j+jdir[k],m,n,path+dir[k],paths,visited,idir,jdir,dir)
    visited[i][j]=False


maze = [[1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1]]

m = len(maze)
n = len(maze[0])
paths = []
visited = [[False for j in range(n)] for i in range(m)]
ratInMaze(maze,0,0,m,n,'',paths,visited)
print(paths)
