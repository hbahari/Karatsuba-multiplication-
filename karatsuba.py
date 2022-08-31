# an implementation of Karatsuba's multiplication algorithm
# this algorithm runs in O(n^2) time

import math


def karatsuba(A, B):
    A_str = str(A)
    B_str = str(B)
    n = len(str(A_str))
    m = len(str(B_str))

    if m < n:  # making the two input lengths equal by padding
        # zeros to the begining of the smaller number

        for i in range(n - m):
            B_str = '0' + B_str
    elif m > n:
        for i in range(m - n):
            A_str = '0' + A_str

    n = len(str(A_str))
    m = len(str(B_str))

    if n == m and n == 1:
        return int(A) * int(B)

    if n > 1:
        a = int(A / math.pow(10, n / 2))
        b = int(A % math.pow(10, n / 2))
        c = int(B / math.pow(10, n / 2))
        d = int(B % math.pow(10, n / 2))

        return (math.pow(10, n) * karatsuba(a, c) + math.pow(10, n / 2) * (
                karatsuba(a, d) + karatsuba(b, c)) + karatsuba(b, d))


A = 3141592653589793238462643383279502884197169399375105820974944592
B = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(A, B))
