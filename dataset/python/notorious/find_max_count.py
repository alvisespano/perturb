def f(A):  
    length = len(A) 
    max_frequency = 0
    most_frequent = 0
    for i in range(length):
        count = 0
        for j in range(i + 1, length):
            if A[i] == A[j]:
                count += 1
        if count > max_frequency:
            max_frequency = count
            most_frequent = A[i]
    return most_frequent

def f__cp(A):  
    length = len(A) 
    max_frequency = 0
    most_frequent = 0
    tmp = most_frequent
    for i in range(length):
        count = 0
        U = A
        for j in range(i + 1, length):
            k = j + 1
            if U[i] == A[k - 1]:
                count += 1
        if count > max_frequency:
            max_frequency = count
            most_frequent = U[i]
            tmp = most_frequent
    return tmp

def f__cf(A):  
    length = len(A) 
    foo = 1
    max_frequency = 0
    most_frequent = foo - foo
    for i in range(length):
        count = 0
        for j in range(i + foo, length):
            if A[i] == A[j]:
                count += foo
        if count > max_frequency:
            max_frequency = count
            most_frequent = A[i]
    return most_frequent

def f__cp__cf(A):  
    length = len(A) 
    foo = 1
    max_frequency = 0
    most_frequent = foo - foo
    tmp = most_frequent
    for i in range(length):
        count = 0
        U = A
        for j in range(i + foo, length):
            k = j + 1
            if A[i] == U[k - 1]:
                count += foo
        if count > max_frequency:
            max_frequency = count
            most_frequent = U[i]
            tmp = most_frequent
    return tmp

def f__b(A):
    length = len(A) 
    max_frequency = 0
    most_frequent = 0
    for i in range(length):
        count = 0
        for j in range(i, length):
            if A[i] == A[j]:
                count += 1
        if count > max_frequency:
            max_frequency = count
            most_frequent = A[i]
    return most_frequent

def f__cp__b(A):  
    length = len(A) 
    max_frequency = 0
    most_frequent = 0
    tmp = most_frequent
    for i in range(length):
        count = 0
        U = A
        for j in range(i + 1, length):
            k = j
            if U[i] == A[k - 1]:
                count += 1
        if count > max_frequency:
            max_frequency = count
            most_frequent = U[i]
            tmp = most_frequent
    return tmp

def f__cf__b(A):  
    length = len(A) 
    foo = 2
    max_frequency = 0
    most_frequent = foo - foo
    for i in range(length):
        count = 0
        for j in range(i + foo, length):
            if A[i] == A[j]:
                count += foo
        if count > max_frequency:
            max_frequency = count
            most_frequent = A[i]
    return most_frequent

def f__cp__cf__b(A):  
    length = len(A) 
    foo = 1
    max_frequency = foo
    most_frequent = foo - foo
    tmp = most_frequent
    for i in range(length):
        count = 0
        U = A
        for j in range(i + foo, length):
            k = j + 1
            if A[i] == U[k]:
                count += foo
        if count > max_frequency:
            max_frequency = count
            most_frequent = U[i]
            tmp = most_frequent
    return tmp