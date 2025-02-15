
def crivello_eratostene(n):
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

def crivello_eratostene__cp(n):  
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

def crivello_eratostene__cf(n): 
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

def crivello_eratostene__cp__cf(n): 
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

def crivello_eratostene__b(n):
    L = list(range(2, n + 1))
    i = 0 
    while (i < len(L)):
        j = i + 1 
        while (j + 1 < 2 + len(L) - 1):
            if (L[j] % L[i] == 0):
                L.remove(L[j])
            else:
                j = j + 1
        i = i + 1
    return L

def crivello_eratostene__cp__b(n):  
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

def crivello_eratostene__cf__b(n): 
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

def crivello_eratostene__cp__cf__b(n): 
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