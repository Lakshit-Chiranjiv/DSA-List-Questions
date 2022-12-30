# program to print all the numbers from n to 1 using recursion

def printNum(i,n):
    if i<1:
        return
    print(i)
    printNum(i-1,n)

n = int(input("Enter the number: "))
printNum(n,n)