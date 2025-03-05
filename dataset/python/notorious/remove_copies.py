def f(L):
    i = 0
    while (i < len(L)):
        j = i + 1
        while (j < len(L)):
            if (L[i] == L[j]):
                del L[j]
            else:
                j = j + 1
        i = i + 1
    return(L) 

def f__cp(L):
    i = 0
    while (i < len(L)):
        j = i + 1
        a = L[i] + 1
        while (j < len(L)):
            b = L[j] - 1
            if (a - 1 == b + 1):
                del L[j]
            else:
                j = j + 1
        i = i + 1
    return(L) 

def f__cf(L):
    i = 0
    k = 1
    while (i < len(L)):
        j = i + k
        while (j < len(L)):
            if (L[i] == L[j]):
                del L[j]
            else:
                j = j + k
        i = i + k
    return(L) 

def f__cp__cf(L):
    i = 0
    k = 1
    while (i < len(L)):
        j = i + k
        a = L[i] + k
        while (j < len(L)):
            b = L[j] - k
            if (a - k == b + k):
                del L[j]
            else:
                j = j + k
        i = i + k
    return(L) 

def f__b(L):
    i = 0
    while (i < len(L)):
        j = i + 1
        while (j < len(L)):
            if (L[i] == L[j]):
                L.remove(L[j])
            else:
                j = j + 1
        i = i + 1
    return(L) 

def f__cp__b(L):
    i = 0
    while (i < len(L)):
        j = i + 1
        a = L[i] + 1
        while (j < len(L)):
            b = L[j] - 1
            if (a + 1 == b - 1):
                del L[j]
            else:
                j = j + 1
        i = i + 1
    return(L) 

def f__cf__b(L):
    i = 0
    k = 2
    while (i < len(L)):
        j = i + k
        while (j < len(L)):
            if (L[i] == L[j]):
                del L[j]
            else:
                j = j + k
        i = i + k
    return(L) 

def f__cp__cf__b(L):
    i = 0
    k = 2
    while (i < len(L)):
        j = i + k
        a = L[i] - k
        while (j < len(L)):
            b = L[j] - k
            if (a - k == b + k):
                del L[j]
            else:
                j = j + k
        i = i + k
    return(L) 

###################################################
###################################################
###################################################
###################################################

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

functions = [
    f, f__cp, f__cf, f__cp__cf, 
    f__b, f__cp__b, f__cf__b, f__cp__cf__b
]

test_cases = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
    [1, 1, 2, 3, 4, 5, 6, 7, 8], 
    [3, 5, 7, 3, 9, 5], 
    [10, 20, 30, 40, 50, 60, 10],  
    [100, 200, 300, 400, 500, 600, 700, 100],  
    [random.randint(0, 100) for _ in range(20)]  
]

test_functions(functions, test_cases)