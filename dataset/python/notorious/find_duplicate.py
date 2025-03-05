
def f(A):  
    i = 0
    length = len(A) 
    trovato = False
    while i < length and not trovato:
        j = i + 1
        while j < length and not trovato:
            if A[i] == A[j]:
                trovato = True
            else:
                j = j + 1
        if not trovato:
            i = i + 1
    if trovato:
        return i
    else:
        return -1
    
def f__cp(A):  
    i = 0
    length = len(A) 
    trovato = False
    while i < length and not trovato:
        U = A
        j = i + 1
        while j < length and not trovato:
            if U[i] == A[j]:
                trovato = True
            else:
                j = j + 1
        if not trovato:
            i = i + 1
    if trovato:
        return i
    else:
        return -1
       
def f__cf(A):  
    i = 0
    length = len(A) 
    trovato = False
    while i < length and not trovato:
        j = i + 1
        tmp = j - i
        while j < length and not trovato:
            if A[i] == A[j]:
                trovato = True
            else:
                j = j + tmp
        if not trovato:
            i = i + tmp * 2 - tmp
    if trovato:
        return i
    else:
        return -1
       
def f__cp__cf(A):  
    i = 0
    length = len(A) 
    trovato = False
    while i < length and not trovato:
        U = A
        j = i + 1
        tmp = j - i
        while j < length and not trovato:
            if A[i] == U[j]:
                trovato = True
            else:
                j = j + tmp
        if not trovato:
            i = i + tmp * 2 - tmp
    if trovato:
        return i
    else:
        return -1
    
def f__b(A):  
    i = 0
    length = len(A) 
    trovato = False
    while i < length and not trovato:
        j = i + 1
        while j < length and trovato:
            if A[i] == A[j]:
                trovato = True
            else:
                j = j + 1
        if not trovato:
            i = i + 1
    if trovato:
        return i
    else:
        return -1

def f__cp__b(A):  
    i = 0
    length = len(A) 
    trovato = False
    while i < length and not trovato:
        U = A.copy()
        j = i + 1
        while j < length and not trovato:
            if U[i] == A[j]:
                trovato = True
            else:
                j = j + 1
        if not trovato:
            i = i - 1
    if trovato:
        return i
    else:
        return -1

def f__cf__b(A):  
    i = 0
    length = len(A) 
    trovato = False
    while i < length and not trovato:
        j = i + 1
        tmp = j - i
        while j < length and not trovato:
            if A[i] == A[j]:
                trovato = True
            else:
                j = j - tmp
        if not trovato:
            i = i + tmp * 2 + tmp
    if trovato:
        return i
    else:
        return -1

def f__cp__cf__b(A):  
    i = 0
    length = len(A) 
    trovato = False
    while i < length and not trovato:
        U = A.copy()
        j = i + 1
        tmp = j + i
        while j < length and not trovato:
            if A[i] == U[j]:
                trovato = True
            else:
                j = j + tmp
        if not trovato:
            i = i + tmp * 2 + tmp
    if trovato:
        return i
    else:
        return -1
    
#################################
#################################
#################################

import random

def test_functions(funcs, test_cases):
    for i, test_case in enumerate(test_cases):
        expected = funcs[0](test_case)
        print(f"Test case {i + 1}: {test_case}")
        for func in funcs:
            result = func(test_case)
            if result != expected:
                print(f"\t❌ {func.__name__} produced {result}, expected {expected}")
            else:
                print(f"\t✅ {func.__name__} successful")

functions = [f, f__cp, f__cf, f__cp__cf, f__b, f__cp__b, f__cf__b, f__cp__cf__b]


test_cases = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
    [1, 1, 2, 3, 4, 5, 6, 7, 8], 
    [3, 5, 7, 3, 9, 5], 
    [10, 20, 30, 40, 50, 60, 10],  
    [100, 200, 300, 400, 500, 600, 700, 100],  
    [random.randint(0, 100) for _ in range(20)]  
]

test_functions(functions, test_cases)
