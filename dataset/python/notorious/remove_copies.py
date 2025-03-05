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

