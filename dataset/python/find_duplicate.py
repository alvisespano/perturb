def find_duplicate(A):  # ritorna la posizione del primo elemento che occorre almeno 2 volte
    i = 0
    length = len(A) 
    trovato = False
    while ((i < length) and not trovato):
        j = i+1
        while ((j < length) and not trovato):
            if (A[i] == A[j]):
                trovato = True
            else:
                j = j+1
        if (not trovato):
            i = i+1
    if (trovato):
        return(i)
    else:
        return(-1)