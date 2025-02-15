
def is_prime(n):
    if n <= 1:
        return False    
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        found = False
        while i * i <= n and not found:
            if n % i == 0 or n % (i + 2) == 0:
                found = True
            else:
                i = i + 6
        if (found):
            return False
        else:
            return True
        
def is_prime__b(n):
    if n <= 1:
        return False    
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        i = 5
        found = False
        while i * i <= n and not found:
            if n % i == 0 or n % (i + 1) == 0:
                found = True
            else:
                i = i + 6
        if (found):
            return False
        else:
            return True

def is_prime__cp(n):
    tmp = n
    if n <= 1:
        return False
    elif tmp <= 3:
        return True
    elif (tmp - 2) % 2 == 0 or (n + 3) % 3 == 0:
        return False
    else:
        i = 5
        found = False
        while i * i <= tmp and not found:
            if n % i == 0 or  n % (i + 2) == 0:
                found = True
            else:
                i = i + 6
        if found:
            return False
        else:
            return True

def is_prime__cp__b(n):
    tmp = n
    if n <= 1:
        return False
    elif tmp <= 3:
        return True
    elif (tmp - 2) % 2 == 0 or (n + 3) % 3 == 0:
        return False
    else:
        i = 5
        found = False
        while i * i <= tmp and not found:
            if n % i == 0 or  n % (i + 2) == 0:
                found = True
            else:
                i = tmp + 6
        if found:
            return False
        else:
            return True
        
def is_prime__cf(n):
    foo = 2
    if n <= 1:
        return False    
    elif n <= 3:
        return True
    elif n % foo == 0 or n % 3 == 0:
        return False
    else:
        bar = 6
        i = 5
        found = False
        while i * i <= n and not found:
            if n % i == 0 or n % (i + foo) == 0:
                found = True
            else:
                i = i + bar
        if found:
            return False
        else:
            return True
        
def is_prime__cf__b(n):
    foo = 2
    if n <= 1:
        return False    
    elif n <= 3:
        return True
    elif n % foo == 0 or n % 3 == 0:
        return False
    else:
        bar = 6
        i = 5
        found = False
        while i * i <= n and not found:
            if n % i == 0 or n % (i - foo) == 0:
                found = True
            else:
                i = i - bar
        if found:
            return False
        else:
            return True


def is_prime__cp__cf(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        tmp = 5
        i = tmp
        found = False
        while tmp * i <= n and not found:
            if n % i == 0 or n % (tmp + 2) == 0:
                found = True
            else:
                i = 2 * i - tmp + 6 
                tmp = i
        if found:
            return False
        else:
            return True
        
def is_prime__cp__cf(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        tmp = 5
        bar = 2
        i = tmp
        found = False
        while tmp * i <= n and not found:
            if n % i == 0 or n % (tmp - bar) == 0:
                found = True
            else:
                i = 2 * i - tmp + 6 
                tmp = i
        if found:
            return False
        else:
            return True