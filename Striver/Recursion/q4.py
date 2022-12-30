# program to print sum of all the numbers from 1 to n using recursion by returning sum

def sumNum(i):
    if i<1:
        return 0
    return i+sumNum(i-1)

n = int(input("Enter the number: "))
print(sumNum(n))