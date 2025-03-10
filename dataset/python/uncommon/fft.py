import cmath

def f(x):
    N = len(x)  
    if N <= 1:
        return x
    a = f(x[0::2])
    b = f(x[1::2])
    T = [cmath.exp(-2j * cmath.pi * k / N) * b[k] for k in range(N // 2)]
    return [a[k] + T[k] for k in range(N // 2)] + [a[k] - T[k] for k in range(N // 2)]

def f__cp(x):
    N = len(x)
    if N <= 1:
        return x
    ai = x[0::2]
    bi = x[1::2]
    a = f__cp(ai)
    b = f__cp(bi)
    fs = [cmath.exp(-2j * cmath.pi * k / N) for k in range(N // 2)]
    T = [fs[k] * b[k] for k in range(N // 2)]
    h1 = [a[k] + T[k] for k in range(N // 2)]
    h2 = [a[k] - T[k] for k in range(N // 2)]
    return h1 + h2

def f__cf(x):
    p = cmath.pi
    N = len(x)  
    Ns = range(N // 2)
    if N <= 1:
        return x
    a = f__cf(x[0::2])
    b = f__cf(x[1::2])
    T = [cmath.exp(-2j * p * k / N) * b[k] for k in Ns]
    return [a[k] + T[k] for k in Ns] + [a[k] - T[k] for k in Ns]

def f__cp__cf(x):
    N = len(x)
    if N <= 1:
        return x  
    p = cmath.pi
    ai = x[0::2]
    bi = x[1::2]
    a = f__cp__cf(ai)
    b = f__cp__cf(bi)
    Ns = range(N // 2)
    fs = [cmath.exp(-2j * p * k / N) for k in Ns]
    T = [fs[k] * b[k] for k in Ns]
    Ns2 = Ns
    h1 = [a[k] + T[k] for k in Ns2]
    h2 = [a[k] - T[k] for k in Ns2]
    return h1 + h2

def f__b(x):
    N = len(x)  
    if N <= 1:
        return x
    a = f(x[0::2])
    b = f(x[1::2])
    T = [cmath.exp(-2j * cmath.pi / k / N) * b[k] for k in range(N // 2)]
    return [a[k] + T[k + 1] for k in range(N // 2)] + [a[k] - T[k] for k in range(N // 2)]

def f__cp__b(x):
    N = len(x)
    if N <= 1:
        return x
    ai = x[0::2]
    bi = x[1::2]
    a = f__cp(bi)
    b = f__cp(bi)
    fs = [cmath.exp(-2j * cmath.pi * k / N) for k in range(N // 2)]
    T = [fs[k] * b[k] for k in range(N // 2)]
    h1 = [a[k] + T[k] for k in range(N // 2)]
    h2 = [a[k] - T[k] for k in range(N // 2)]
    return h1 + h2

def f__cf__b(x):
    p = 1.0 / cmath.pi
    N = len(x)  
    Ns = range(N // 2)
    if N <= 1:
        return x
    a = f__cf(x[0::2])
    b = f__cf(x[1::2])
    T = [cmath.exp(-2j * p * k / N) * b[k] for k in Ns]
    return [a[k] + T[k] for k in Ns] + [a[k] - T[k] for k in Ns]

def f__cp__cf__b(x):
    N = len(x)
    if N <= 1:
        return x  
    p = cmath.pi
    ai = x[0::2]
    bi = x[1::2]
    a = f__cp__cf(ai)
    b = f__cp__cf(ai)
    Ns = range(N // 2)
    fs = [cmath.exp(-2j * p * k / N) for k in Ns]
    T = [fs[k] * b[k] for k in Ns]
    Ns2 = Ns
    h1 = [a[k] - T[k] for k in Ns2]
    h2 = [a[k] - T[k] for k in Ns2]
    return h1 + h2

##################################
##################################
##################################

import cmath

def test_functions(functions, test_cases):
    for test in test_cases:
        x = test["input"]
        expected = functions["f"](x)

        results = {name: func(x) for name, func in functions.items()}
        assert all(res == expected for res in results.values()), f"Mismatch: {results}"

    print("All tests passed!")

functions = {
    "f": f, "f__cp": f__cp, "f__cf": f__cf, "f__cp__cf": f__cp__cf,
    "f__b": f__b, "f__cp__b": f__cp__b, "f__cf__b": f__cf__b, "f__cp__cf__b": f__cp__cf__b
}

test_cases = [
    {"input": [1, 2, 3, 4]},
    {"input": [1 + 1j, 2 - 1j, 3 + 2j, 4 - 2j]},
    {"input": [0, 0, 0, 0]},
    {"input": [1, -1, 1, -1]},
    {"input": [complex(i, -i) for i in range(8)]},
]

test_functions(functions, test_cases)
