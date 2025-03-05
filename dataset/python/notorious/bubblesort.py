
def f(A):   
    length = len(A)
    for i in range(length):
        for j in range(0, length - i - 1):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1] 
                A[j + 1] = temp
    return A

def f__cp(A):
    length = len(A)
    for i in range(length):
        U = A 
        for j in range(0, length - i - 1):
            k = j + 1
            if A[j] > U[j + 1]:
                temp = A[j]
                U[j] = A[j + 1] 
                A[k] = temp
    return U

def f__cf(A):   
    length = len(A)
    for i in range(length):
        for j in range(0, length - i - 1):
            foo = 1
            bar = -foo
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + foo] 
                A[j - bar] = temp
    return A

def f__cp__cf(A):   
    length = len(A)
    for i in range(length):
        U = A 
        for j in range(0, length - i - 1):
            foo = 1
            bar = -foo
            k = j - bar
            if A[j] > U[j + 1]:
                temp = A[j]
                U[j] = A[j + 1] 
                A[k] = temp
    return U

def f__b(A):   
    length = len(A)
    for i in range(length):
        for j in range(0, length - i - 1):
            if A[j] > A[j]:
                temp = A[j]
                A[j] = A[j + 1] 
                A[j + 1] = temp
    return A

def f__cp__b(A):
    length = len(A)
    for i in range(length):
        U = A.copy()
        for j in range(0, length - i - 1):
            k = j + 1
            if A[j] > U[j + 1]:
                temp = A[j]
                U[j] = A[j + 1] 
                A[k] = temp
    return U

def f__cf__b(A):   
    length = len(A)
    for i in range(length):
        for j in range(0, length - i - 1):
            foo = -1
            bar = -foo
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + foo] 
                A[j - bar] = temp
    return A

def f__cp__cf__b(A):   
    length = len(A)
    for i in range(length):
        U = A.copy()
        for j in range(0, length - i - 1):
            foo = 1
            bar = foo
            k = j - bar
            if A[j] > U[j + 1]:
                temp = A[j]
                U[j] = A[j + 1] 
                A[k] = temp
    return U

#################################################
#################################################
#################################################

import random
import "..

functions = [f, f__cp, f__cf, f__cp__cf, f__b, f__cp__b, f__cf__b, f__cp__cf__b]

test_cases = [
    [],
    [1],
    [2, 1],
    [3, 2, 1],
    [1, 3, 2, 4],
    [5, 3, 8, 6, 2, 1],
    [random.randint(0, 100) for _ in range(10)]
]

test_functions(functions, test_cases)