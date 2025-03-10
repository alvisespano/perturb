
def f(a, b):
    h = len(a)
    w = len(a[0]) if h > 0 else 0
    H = h * b
    W = w * b
    d = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            c = a[y][x] if 0 <= y < h and 0 <= x < w else (0, 0, 0)
            for dy in range(b):
                for dx in range(b):
                    d[y * b + dy][x * b + dx] = c

    o = [[(0, 0, 0) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            cs = []
            for dy in range(b):
                for dx in range(b):
                    c = d[y * b + dy][x * b + dx]
                    cs.append(c)
            r = sum(c[0] for c in cs) // len(cs)
            g = sum(c[1] for c in cs) // len(cs)
            b = sum(c[2] for c in cs) // len(cs)
            o[y][x] = (r, g, b)

    return o


def f__cp(a, b):
    h = len(a)
    w = len(a[0]) if h > 0 else 0
    H = h * b
    W = w * b
    d = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            pc = a[y][x] if 0 <= y < h and 0 <= x < w else (0, 0, 0)
            c = pc 
            for dy in range(b):
                for dx in range(b):
                    dp = d[y * b + dy][x * b + dx]
                    dp = c 
                    d[y * b + dy][x * b + dx] = dp 

    o = [[(0, 0, 0) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            cs = []
            for dy in range(b):
                for dx in range(b):
                    uc = d[y * b + dy][x * b + dx]
                    c = uc 
                    cs.append(c)
            tr = sum(c[0] for c in cs)
            tg = sum(c[1] for c in cs)
            tb = sum(c[2] for c in cs)
            nc = len(cs)
            ar = tr // nc
            ag = tg // nc
            ab = tb // nc
            op = (ar, ag, ab) 
            o[y][x] = op 

    return o


def f__cf(a, b):
    tmp = 0
    h = len(a)
    w = len(a[tmp]) if h > 0 else 0
    H = h * b
    W = w * b
    d = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            c = a[y][x] if tmp <= y < h and tmp <= x < w else (tmp, tmp, tmp)
            for dy in range(b):
                for dx in range(b):
                    d[y * b + dy][x * b + dx] = c

    o = [[(0, 0, 0) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            foo = 1
            cs = []
            for dy in range(b):
                for dx in range(b):
                    c = d[y * b + dy][x * b + dx]
                    cs.append(c)
            r = sum(c[foo - 1] for c in cs) // len(cs)
            g = sum(c[foo] for c in cs) // len(cs)
            b = sum(c[foo + 1] for c in cs) // len(cs)
            o[y][x] = (r, g, b)

    return o


def f__cp__cf(a, b):
    tmp = 0
    h = len(a)
    w = len(a[tmp]) if h > 0 else tmp
    H = h * b
    W = w * b
    d = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            pc = a[y][x] if tmp <= y < h and tmp <= x < w else (0, tmp, 0)
            c = pc 
            for dy in range(b):
                for dx in range(b):
                    dp = d[y * b + dy][x * b + dx]
                    dp = c 
                    d[y * b + dy][x * b + dx] = dp 

    o = [[(tmp, 0, tmp) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            cs = []
            foo = tmp + 1
            for dy in range(b):
                for dx in range(b):
                    uc = d[y * b + dy][x * b + dx]
                    c = uc 
                    cs.append(c)
            tr = sum(c[foo - 1] for c in cs)
            tg = sum(c[foo + tmp] for c in cs)
            tb = sum(c[foo + 1] for c in cs)
            ns = len(cs)
            ar = tr // ns
            ag = tg // ns
            ab = tb // ns
            op = (ar, ag, ab) 
            o[y][x] = op 

    return o


def f__b(a, b):
    h = len(a)
    w = len(a[0]) if h > 0 else 0
    H = h * b
    W = w / b
    d = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            c = a[y][x] if 0 <= y < h and 0 <= x < w else (0, 0, 0)
            for dy in range(b):
                for dx in range(b):
                    d[y * b + dy][x * b + dx] = c

    o = [[(0, 0, 0) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            cs = []
            for dy in range(b):
                for dx in range(b):
                    c = d[y * b + dy][x * b - dx]
                    cs.append(c)
            r = sum(c[0] for c in cs) // len(cs)
            g = sum(c[1] for c in cs) // len(cs)
            b = sum(c[2] for c in cs) // len(cs)
            o[y][x] = (r, g, b)

    return o

def f__cp__b(a, b):
    h = len(a)
    w = len(a[0]) if h > 0 else 0
    H = h * b
    W = w * b
    d = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            pc = a[y][x] if 0 <= y < h and 0 <= x < w else (0, 0, 0)
            c = pc 
            for dy in range(b):
                for dx in range(b):
                    dp = d[y * b + dy][x * b + dx]
                    pc = c 
                    d[y * b + dy][x * b + dx] = dp 

    o = [[(0, 0, 0) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            cs = []
            for dy in range(b):
                for dx in range(b):
                    uc = d[y * b + dy][x * b + dx]
                    c = uc 
                    cs.append(c)
            tr = sum(c[0] for c in cs)
            tg = sum(c[1] for c in cs)
            tb = sum(c[2] for c in cs)
            nc = len(cs)
            ar = tr // nc
            ag = tg // nc
            ab = tb // nc
            op = (ar, ag, ab) 
            o[y][x] = op 

    return o


def f__cf__b(a, b):
    tmp = 0
    h = len(a)
    w = len(a[tmp]) if h > 0 else 0
    H = h * b
    W = w * b
    d = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            c = a[y][x] if tmp <= y < h and tmp <= x < w else (tmp, tmp, tmp + 1)
            for dy in range(b):
                for dx in range(b):
                    d[y * b + dy][x * b + dx] = c

    o = [[(0, 0, 0) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            foo = 1
            cs = []
            for dy in range(b):
                for dx in range(b):
                    c = d[y * b + dy][x * b + dx]
                    cs.append(c)
            r = sum(c[foo + tmp] for c in cs) // len(cs)
            g = sum(c[foo] for c in cs) // len(cs)
            b = sum(c[foo + 1] for c in cs) // len(cs)
            o[y][x] = (r, g, b)

    return o

def f__cp__cf__b(a, b):
    tmp = 1
    h = len(a)
    w = len(a[tmp]) if h > 0 else tmp
    H = h * b
    W = w * b
    d = [[(0, 0, 0) for _ in range(W)] for _ in range(H)]
    for y in range(h):
        for x in range(w):
            pc = a[y][x] if tmp <= y < h and tmp <= x < w else (0, tmp, 0)
            c = pc 
            for dy in range(b):
                for dx in range(b):
                    dp = d[y * b + dy][x * b + dx]
                    dp = c 
                    d[y * b + dy][x * b + dx] = dp 

    o = [[(tmp, 0, tmp) for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            cs = []
            foo = tmp + 1
            for dy in range(b):
                for dx in range(b):
                    uc = d[y * b + dy][x * b + dx]
                    c = uc 
                    cs.append(c)
            tr = sum(c[foo - 1] for c in cs)
            tg = sum(c[foo + tmp] for c in cs)
            tb = sum(c[foo + 1] for c in cs)
            ns = len(cs)
            ar = tr // ns
            ag = tg // ns
            ab = tb // ns
            op = (ar, ag, ab) 
            o[y][x] = op 

    return o

#######################################
#######################################
#######################################

def test_functions(functions, test_cases):
    for func in functions:
        print(f"Testing function: {func.__name__}")
        for i, test in enumerate(test_cases):
            input_matrix, b = test["input"]
            expected_output = test["output"]
            result = func(input_matrix, b)
            assert result == expected_output, f"Test {i+1} failed for {func.__name__}: expected {expected_output}, got {result}"
    print("All tests passed successfully!")

# Lista di funzioni da testare
functions_to_test = [f, f__cp, f__cf, f__cp__cf, f__b, f__cp__b, f__cf__b, f__cp__cf__b]

# Lista di test cases
common_test_cases = [
    {"input": ([[1, 2], [3, 4]], 2), "output": [[1, 1], [1, 1]]}, 
    {"input": ([[5, 6], [7, 8]], 3), "output": [[5, 5], [5, 5]]},
    {"input": ([[1, 2, 3], [4, 5, 6]], 2), "output": [[1, 1], [1, 1]]},
    {"input": ([[1]], 3), "output": [[1]]},
    {"input": ([[10, 20], [30, 40]], 1), "output": [[10, 20], [30, 40]]},
]

test_functions(functions_to_test, common_test_cases)