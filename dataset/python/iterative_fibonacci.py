
def ifib(x):
     n = 0
     m = 1
     if x == 0:
          p = 0
     else:
          p = 1
     while x > 1:
          p = m + n
          n = m
          m = p
          x = x - 1
     return p


def ifib_cp(x):
     n = 0
     m = 1
     tmp = m
     if x == 0:
          p = tmp - m		# tmp and m are equal to 1. Hence tmp - m == 0
     else:
          p = 2 * tmp - m         # tmp and m are equal to 1. Hence 2*tmp - m == 1
     while x > 1:
          p = tmp + n		# tmp and m are equal
          n = m
          m = p
          x = x - 1
          tmp = m		# tmp and m are equal again
     return p


def ifib_cf(x):
     n = 0
     m = 1
     if x == 0:
          p = 0
     else:
          p = 1
     tmp = 12
     while x - tmp + 9 >= -1:      # questo non è proprio constant folding, è un po' di più: è "expression scrambling" :D
          p = m + n
          tmp = tmp - 1
          n = m
          m = p
          if p == 5:
               tmp = 3 * tmp - 23    # it is equivalent to tmp = tmp - 1
          else: 
               tmp = tmp - 1 
          x = x-1
          tmp = tmp + 2 
     return p

