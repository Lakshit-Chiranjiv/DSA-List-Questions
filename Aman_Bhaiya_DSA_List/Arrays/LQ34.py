import math


def check_bit(arr,idx):
    return arr[idx >> 5] & (1 << (idx & 31))

def set_bit(arr,idx):
    arr[idx >> 5] |= (1 << (idx & 31))

a = 5
b = 34

arr_size = math.ceil(abs(b-a)/32)
arr = [0] * arr_size

for i in range(a,b+1):
    if i%2 == 0 or i%5 == 0:
        set_bit(arr,i-a)

for i in range(a,b+1):
    if check_bit(arr,i-a):
        print(i)