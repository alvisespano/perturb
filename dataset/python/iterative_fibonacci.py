
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


def ifib__cp(x):
     n = 0
     m = 1
     tmp = m
     if x == 0:
          p = tmp - m		
     else:
          p = 2 * tmp - m    
     while x > 1:
          p = tmp + n
          n = m
          m = p
          x = x - 1
          tmp = m	
     return p


def ifib__cf(x):
     n = 0
     m = 1
     if x == 0:
          p = 0
     else:
          p = 1
     tmp = 12
     while x - tmp + 9 >= -1: 
          p = m + n
          tmp = tmp - 1
          n = m
          m = p
          if p == 5:
               tmp = 3 * tmp - 23  
          else: 
               tmp = tmp - 1 
          x = x-1
          tmp = tmp + 2 
     return p

