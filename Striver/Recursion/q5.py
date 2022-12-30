# program to print all the numbers from 1 to n using recursion backtracking

def printNum(i,n):
    if i < 1:
        return
    printNum(i-1,n)
    print(i)

n = int(input("Enter the number: "))
printNum(n,1)