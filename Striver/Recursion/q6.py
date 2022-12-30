# program to print all the numbers from n to 1 using recursion backtracking

def printNum(i,n):
    if i > n:
        return
    printNum(i+1,n)
    print(i)

n = int(input("Enter the number: "))
printNum(1, n)