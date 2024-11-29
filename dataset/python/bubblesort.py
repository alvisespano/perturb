def fun(A):  # ritorna la posizione del primo elemento che occorre almeno 2 volte
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


def bs(A):   # funzione bubblesort
    length = len(A)
    for i in range(length):
        for j in range(0, length - i - 1):
            if (A[j] > A[j + 1]):
                temp = A[j]
                A[j] = A[j + 1] 
                A[j + 1] = temp
    return(A)

def mfe(A):   # ritorna il primo elemento dell'array con il maggior numero di occorrenze
    length = len(A) 
    max_frequency = 0
    most_frequent = 0
    for i in range(length):
        count = 0 ;
        for j in range(i+1,length):
            if (A[i] == A[j]):
                count += 1
        if (count > max_frequency):
            max_frequency = count
            most_frequent = A[i]
    return most_frequent