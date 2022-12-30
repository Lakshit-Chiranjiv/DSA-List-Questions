# program to print all the numbers from 1 to n using recursion

def printNum(i,n):
    if i>n:
        return
    print(i)
    printNum(i+1,n)

n = int(input("Enter the number: "))
printNum(1,n)
