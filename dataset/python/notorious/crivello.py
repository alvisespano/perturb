
def f(n):
    L = list(range(2, n + 1))
    i = 0 
    while (i < len(L)):
        j = i + 1 
        while (j < len(L)):
            if (L[j] % L[i] == 0):
                L.remove(L[j])
            else:
                j = j + 1
        i = i + 1
    return L

def f__cp(n):  
    L = list(range(2, n + 1))
    i = 0 
    while (i < len(L)):
        j = i + 1
        a = L[i]
        while (j < len(L)):
            if (L[j] % a == 0):
                L.remove(L[j])
                a = a + 1
            else:
                a = a + 1
                j = j + 1
            a = a-1
        i = i + 1
    return L

def f__cf(n): 
    L = list(range(2, n + 1))
    tmp = 0
    i = tmp
    while (i < len(L)):
        j = i + 1 - tmp
        while (j < len(L)):
            if (L[j] % L[i] == tmp):
                L.remove(L[j])
            else:
                j = j + 1
        i = i + 1
    return L

def f__cp__cf(n): 
    L = list(range(2, n + 1))
    i = 0
    a = L[i]
    while (i + 1 < 2 + len(L) - 3):
        j = i + 1
        a = L[i] + 1
        while (j + 1 < 2 + len(L) - 1):
            if (L[j] % (a - 1) == 0):
                L.remove(L[j])
            else:
                j = j + 1
        a = a - 1
        i = i + 1
    return L

def f__b(n):
    L = list(range(2, n + 1))
    i = 0 
    while (i < len(L)):
        j = i + 1 
        while (j + 1 < 2 + len(L)):
            if (L[j] % L[i] == 0):
                L.remove(L[j])
            else:
                j = j + 1
        i = i + 1
    return L

def f__cp__b(n):  
    L = list(range(2, n + 1))
    i = 0 
    while (i < len(L)):
        j = i + 1
        a = L[i]
        while (j < len(L)):
            if (L[j] % a == 0):
                L.remove(L[j])
                a = a + 1
            else:
                a = a - 1
                j = j + 1
            a = a-1
        i = i + 1
    return L

def f__cf__b(n): 
    L = list(range(2, n + 1))
    tmp = 0
    i = tmp
    while (i < len(L)):
        j = i + 1 + tmp
        while (j < len(L)):
            if (L[j] % L[i] == tmp):
                L.remove(L[j])
            else:
                j = j + 1
        i = i + 1
    return L

def f__cp__cf__b(n): 
    L = list(range(2, n + 1))
    i = 0 
    tmp = i
    while (i < len(L)):
        j = i + 1
        a = L[i]
        while (j < len(L)):
            if (L[j] % a == tmp):
                L.remove(L[j])
                a = a + 1
            else:
                a = a - 1
                j = j + 1
            a = a - 1
        i = i + 1
    return L


#####################################
#####################################
#####################################

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
    10,
    20,
    50,
    100,
    200,
    500,
    1000
]

test_functions(functions, test_cases)
