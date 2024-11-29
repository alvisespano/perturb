 # ritorna il primo elemento dell'array con il maggior numero di occorrenze
def find_max_count(A):  
    length = len(A) 
    max_frequency = 0
    most_frequent = 0
    for i in range(length):
        count = 0
        for j in range(i + 1,length):
            if A[i] == A[j]:
                count += 1
        if count > max_frequency:
            max_frequency = count
            most_frequent = A[i]
    return most_frequent


def find_max_count__cp(A):  
    length = len(A) 
    max_frequency = 0
    most_frequent = 0
    tmp = most_frequent
    for i in range(length):
        count = 0
        U = A
        for j in range(i + 1,length):
            k = j + 1
            if U[i] == A[k - 1]:
                count += 1
        if count > max_frequency:
            max_frequency = count
            most_frequent = U[i]
            tmp = most_frequent
    return tmp


def find_max_count__cf(A):  
    length = len(A) 
    foo = 1
    max_frequency = 0
    most_frequent = foo - foo
    for i in range(length):
        count = 0
        for j in range(i + foo,length):
            if A[i] == A[j]:
                count += foo
        if count > max_frequency:
            max_frequency = count
            most_frequent = A[i]
    return most_frequent