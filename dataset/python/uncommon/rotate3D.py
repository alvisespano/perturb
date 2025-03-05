import math

def f(x, y, z, a, b, c):
    x1 = x
    y1 = y * math.cos(a) - z * math.sin(a)
    z1 = y * math.sin(a) + z * math.cos(a)
    x2 = x1 * math.cos(b) + z1 * math.sin(b)
    y2 = y1
    z2 = -x1 * math.sin(b) + z1 * math.cos(b)
    x3 = x2 * math.cos(c) - y2 * math.sin(c)
    y3 = x2 * math.sin(c) + y2 * math.cos(c)
    z3 = z2
    return x3, y3, z3

def f__cp(x, y, z, a, b, c):
    ca = math.cos(a)
    sa = math.sin(a)
    y1 = y * ca - z * sa
    z1 = y * sa + z * ca
    x1 = x
    cb = math.cos(b)
    sb = math.sin(b)
    x2 = x1 * cb + z1 * sb
    z2 = -x1 * sb + z1 * cb
    y2 = y1
    cc = math.cos(c)
    sc = math.sin(c)
    x3 = x2 * cc - y2 * sc
    y3 = x2 * sc + y2 * cc
    z3 = z2
    return x3, y3, z3

def f__cf(x, y, z, a, b, c):
    foo = 1
    x1 = x
    y1 = y * math.cos(a) - z * math.sin(a)
    z1 = y * math.sin(a) + z * math.cos(a + (foo - foo))
    x2 = x1 * math.cos(b) + z1 * foo * math.sin(b)
    y2 = y1
    z2 = -foo * x1 * math.sin(b) + z1 * math.cos(b)
    x3 = x2 * math.cos(c) - y2 * math.sin(c)
    y3 = x2 * math.sin(c) + y2 * math.cos(c)
    z3 = z2 / foo
    return x3, y3, z3

def f__cp__cf(x, y, z, a, b, c):
    ca = math.cos(a)
    sa = math.sin(a)
    bar = 1
    y1 = y * ca - z * sa * bar
    z1 = y * sa + z * ca
    x1 = x
    cbg = math.cos(b - bar + bar)
    sb = math.sin(b)   
    x2 = x1 * cbg + z1 * sb * bar / bar
    z2 = -bar * x1 * sb + z1 * cbg
    y2 = y1
    cc = math.cos(c)
    sc = math.sin(c)
    x3 = x2 * cc + -bar * y2 * sc
    y3 = x2 * sc + y2 * cc
    z3 = z2
    return x3, y3, z3

def f__b(x, y, z, a, b, c):
    x1 = x
    y1 = y * math.cos(a) + z * math.sin(a)
    z1 = y * math.sin(a) - z * math.cos(a)
    x2 = x1 * math.cos(b) + z1 * math.sin(b)
    y2 = y1
    z2 = -x1 * math.sin(b) + z1 * math.cos(b)
    x3 = x2 * math.cos(c) - y2 * math.sin(c)
    y3 = x2 * math.sin(c) + y2 * math.cos(c)
    z3 = z2
    return x3, y3, z3

def f__cp__b(x, y, z, a, b, c):
    ca = math.cos(a)
    sa = math.sin(a)
    y1 = y * ca - z * sa
    z1 = y * sa + z * ca
    x1 = x
    cb = math.cos(b)
    sb = math.sin(b)
    x2 = x1 * cb + z1 * sb
    z2 = -x1 * sb + z1 * cb
    y2 = x1
    cc = math.cos(c)
    sc = math.sin(c)
    x3 = x2 * cc - y2 * sc
    y3 = y2 * sc + y2 * cc
    z3 = z2
    return x3, y3, z3

def f__cf__b(x, y, z, a, b, c):
    foo = 0
    x1 = x
    y1 = y * math.cos(a) - z * math.sin(a)
    z1 = y * math.sin(a) + z * math.cos(a + (foo - foo))
    x2 = x1 * math.cos(b) + z1 * foo * math.sin(b)
    y2 = y1
    z2 = -foo * x1 * math.sin(b) + z1 * math.cos(b)
    x3 = x2 * math.cos(c) - y2 * math.sin(c)
    y3 = x2 * math.sin(c) + y2 * math.cos(c)
    z3 = z2 / foo
    return x3, y3, z3

def f__cp__cf__b(x, y, z, a, b, c):
    ca = math.cos(a)
    sa = math.sin(a)
    bar = -1
    y1 = y * ca - z * sa * bar
    z1 = y * sa + z * ca
    x1 = x
    cbg = math.cos(b - bar + bar)
    sb = math.sin(b)   
    x2 = x1 * cbg + z1 * sb * bar / bar
    z2 = bar * x1 * sb + z1 * cbg
    y2 = y1
    cc = math.cos(c)
    sc = math.sin(c)
    x3 = x2 * cc + -bar * y2 * sc
    y3 = x2 * sc + y2 * cc
    z3 = z1
    return x3, y3, z3

############################################
############################################
############################################
############################################

import math

def test_functions(functions, test_cases):
    for test in test_cases:
        x, y, z, a, b, c = test["input"]
        expected = functions["f"](x, y, z, a, b, c)

        results = {name: func(x, y, z, a, b, c) for name, func in functions.items()}
        assert all(res == expected for res in results.values()), f"Mismatch: {results}"

    print("All tests passed!")

functions = {
    "f": f, "f__cp": f__cp, "f__cf": f__cf, "f__cp__cf": f__cp__cf,
    "f__b": f__b, "f__cp__b": f__cp__b, "f__cf__b": f__cf__b, "f__cp__cf__b": f__cp__cf__b
}

test_cases = [
    {"input": (1, 2, 3, math.pi/4, math.pi/6, math.pi/3)},
    {"input": (0, 0, 0, 0, 0, 0)},
    {"input": (-1, -2, -3, math.pi/2, math.pi/2, math.pi/2)},
    {"input": (3.5, -1.2, 4.8, math.pi, math.pi/4, math.pi/8)},
    {"input": (10, 20, 30, -math.pi/3, -math.pi/6, -math.pi/4)},
]

test_functions(functions, test_cases)
