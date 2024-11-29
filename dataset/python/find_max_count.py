def find_max_count(A):   # ritorna il primo elemento dell'array con il maggior numero di occorrenze
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