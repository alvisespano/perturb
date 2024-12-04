def remove_copies(L):
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

 # questa e` completamente sbagliata per la semantica di remove. chatGPT dice che e` uguale a remove_copies
def remove_copies_2(L):
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

def remove_copies__cp__cf(L):
    i = 0
    while (i < len(L)):
        j = i + 1
        a = L[i] + 1
        while (j < len(L)):
            b = L[j] - 1
            if (a-1 == b+1):
                del L[j]
            else:
                j = j + 1
        i = i + 1
    return(L) 

def remove_copies__cp__cf_2(L):    # copy propagation + constant folding: chatGPT fallisce
    i = 0
    while (i < len(L)):
        j = i+1
        a = L[i]+1
        while (j < len(L)):
            b = L[j] - 1
            if (((a-1) % (b+1) == 0) or ((b+1) % (a-1) == 0)):
                if (a != b + 2):
                    j = j + 1
                else:
                    del L[j]
            else:
                j = j + 1
        i = i + 1
    return(L) 