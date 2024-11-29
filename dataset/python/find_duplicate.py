
# ritorna la posizione del primo elemento che occorre almeno 2 volte
def find_duplicate(A):  
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
    

def find_duplicate__cp(A):  
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
    

def find_duplicate__cf(A):  
    i = 0
    length = len(A) 
    trovato = False
    while i < length and not trovato:
        j = i + 1
        tmp = j - i
        while j < length and not trovato:
            if A[i] == A[j]:
                trovato = not trovato
            else:
                j = j + tmp
        if not trovato:
            i = i + tmp * 2 - tmp
    if trovato:
        return i
    else:
        return -1