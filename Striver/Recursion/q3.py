# program to print sum of all the numbers from 1 to n using recursion

def sumNum(i,sum):
    if i<1:
        print(sum)
        return
    sum = sum+i
    sumNum(i-1,sum)

n = int(input("Enter the number: "))
sumNum(n,0)