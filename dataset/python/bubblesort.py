
def bubblesort(A):   # funzione bubblesort
    length = len(A)
    for i in range(length):
        for j in range(0, length - i - 1):
            if (A[j] > A[j + 1]):
                temp = A[j]
                A[j] = A[j + 1] 
                A[j + 1] = temp
    return(A)

def bubblesort_cp(A):   # funzione bubblesort
    length = len(A)
    
    for i in range(length):
        for j in range(0, length - i - 1):
            if (A[j] > A[j + 1]):
                temp = A[j]
                A[j] = A[j + 1] 
                A[j + 1] = temp
    return(A)
