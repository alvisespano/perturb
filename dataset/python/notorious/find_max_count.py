def f(A):  
    length = len(A) 
    max_frequency = 0
    most_frequent = 0
    for i in range(length):
        count = 0
        for j in range(i + 1, length):
            if A[i] == A[j]:
                count += 1
        if count > max_frequency:
            max_frequency = count
            most_frequent = A[i]
    return most_frequent

def f__cp(A):  
    length = len(A) 
    max_frequency = 0
    most_frequent = 0
    tmp = most_frequent
    for i in range(length):
        count = 0
        U = A
        for j in range(i + 1, length):
            k = j + 1
            if U[i] == A[k - 1]:
                count += 1
        if count > max_frequency:
            max_frequency = count
            most_frequent = U[i]
            tmp = most_frequent
    return tmp

def f__cf(A):  
    length = len(A) 
    foo = 1
    max_frequency = 0
    most_frequent = foo - foo
    for i in range(length):
        count = 0
        for j in range(i + foo, length):
            if A[i] == A[j]:
                count += foo
        if count > max_frequency:
            max_frequency = count
            most_frequent = A[i]
    return most_frequent

def f__cp__cf(A):  
    length = len(A) 
    foo = 1
    max_frequency = 0
    most_frequent = foo - foo
    tmp = most_frequent
    for i in range(length):
        count = 0
        U = A
        for j in range(i + foo, length):
            k = j + 1
            if A[i] == U[k - 1]:
                count += foo
        if count > max_frequency:
            max_frequency = count
            most_frequent = U[i]
            tmp = most_frequent
    return tmp

def f__b(A):
    length = len(A) 
    max_frequency = 0
    most_frequent = 0
    for i in range(length):
        count = 0
        for j in range(i, length):
            if A[i] == A[j]:
                count += 1
        if count > max_frequency:
            max_frequency = count
            most_frequent = A[i]
    return most_frequent

def f__cp__b(A):  
    length = len(A) 
    max_frequency = 0
    most_frequent = 0
    tmp = most_frequent
    for i in range(length):
        count = 0
        U = A
        for j in range(i + 1, length):
            k = j
            if U[i] == A[k - 1]:
                count += 1
        if count > max_frequency:
            max_frequency = count
            most_frequent = U[i]
            tmp = most_frequent
    return tmp

def f__cf__b(A):  
    length = len(A) 
    foo = 2
    max_frequency = 0
    most_frequent = foo - foo
    for i in range(length):
        count = 0
        for j in range(i + foo, length):
            if A[i] == A[j]:
                count += foo
        if count > max_frequency:
            max_frequency = count
            most_frequent = A[i]
    return most_frequent

def f__cp__cf__b(A):  
    length = len(A) 
    foo = 1
    max_frequency = foo
    most_frequent = foo - foo
    tmp = most_frequent
    for i in range(length):
        count = 0
        U = A
        for j in range(i + foo, length):
            k = j + 1
            if A[i] == U[k]:
                count += foo
        if count > max_frequency:
            max_frequency = count
            most_frequent = U[i]
            tmp = most_frequent
    return tmp

######################################
######################################
######################################

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
    [8, 8, 8, 1, 1, 1, 1, 5, 5],
    [15, 12, 12, 12, 15, 18, 18, 15],
    [7, 9, 7, 7, 9, 9, 9],
    [3, 3, 3, 1, 1, 2, 2, 2, 2, 5],
    [random.randint(1, 100) for _ in range(30)],
    [100, 200, 300, 400, 100, 100, 200],
    [5, 5, 5, 5, 5, 5, 5],
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
]

test_functions(functions, test_cases)
