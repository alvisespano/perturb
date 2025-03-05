
def f(n):
    if n <= 1:
        return False    
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        found = False
        while i * i <= n and not found:
            if n % i == 0 or n % (i + 2) == 0:
                found = True
            else:
                i = i + 6
        if (found):
            return False
        else:
            return True
        
def f__cp(n):
    tmp = n
    if n <= 1:
        return False
    elif tmp <= 3:
        return True
    elif (tmp - 2) % 2 == 0 or (n + 3) % 3 == 0:
        return False
    else:
        i = 5
        found = False
        while i * i <= tmp and not found:
            if n % i == 0 or  n % (i + 2) == 0:
                found = True
            else:
                i = i + 6
        if found:
            return False
        else:
            return True
       
def f__cf(n):
    foo = 2
    if n <= 1:
        return False    
    elif n <= 3:
        return True
    elif n % foo == 0 or n % 3 == 0:
        return False
    else:
        bar = 6
        i = 5
        found = False
        while i * i <= n and not found:
            if n % i == 0 or n % (i + foo) == 0:
                found = True
            else:
                i = i + bar
        if found:
            return False
        else:
            return True

def f__cp__cf(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        tmp = 5
        i = tmp
        found = False
        while tmp * i <= n and not found:
            if n % i == 0 or n % (tmp + 2) == 0:
                found = True
            else:
                i = 2 * i - tmp + 6 
                tmp = i
        if found:
            return False
        else:
            return True

def f__b(n):
    if n <= 1:
        return False    
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        found = False
        while i * i <= n and not found:
            if n % i == 0 or n % (i + 1) == 0:
                found = True
            else:
                i = i + 6
        if (found):
            return False
        else:
            return True

def f__cp__b(n):
    tmp = n
    if n <= 1:
        return False
    elif tmp <= 3:
        return True
    elif (tmp - 2) % 2 == 0 or (n + 3) % 3 == 0:
        return False
    else:
        i = 5
        found = False
        while i * i <= tmp and not found:
            if n % i == 0 or  n % (i + 2) == 0:
                found = True
            else:
                i = tmp + 6
        if found:
            return False
        else:
            return True

def f__cf__b(n):
    foo = 2
    if n <= 1:
        return False    
    elif n <= 3:
        return True
    elif n % foo == 0 or n % 3 == 0:
        return False
    else:
        bar = 6
        i = 5
        found = False
        while i * i <= n and not found:
            if n % i == 0 or n % (i - foo) == 0:
                found = True
            else:
                i = i - bar
        if found:
            return False
        else:
            return True

def f__cp__cf__b(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        tmp = 5
        bar = 2
        i = tmp
        found = False
        while tmp * i <= n and not found:
            if n % i == 0 or n % (tmp - bar) == 0:
                found = True
            else:
                i = 2 * i - tmp + 6 
                tmp = i
        if found:
            return False
        else:
            return True
        
#####################################
#####################################
#####################################

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
    1,
    2,
    3,
    4,
    5,
    7,
    9,
    11,
    13,
    17,
    19,
    random.randint(100, 1000),
    random.randint(1000, 5000),
]

test_functions(functions, test_cases)
