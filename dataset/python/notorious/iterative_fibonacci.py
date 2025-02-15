
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
     foo = 0
     bar = 1
     n = foo
     m = bar
     if x == 0:
          p = foo
     else:
          p = foo + bar
     while x > bar:
          p = m + n
          n = m
          m = p
          x = x - bar
     return p

def ifib__cp__cf(x):
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

def ifib__b(x):
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

def ifib__cp__b(x):
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
          tmp = n
     return p

def ifib__cf__b(x):
     foo = 0
     bar = 1
     n = foo
     m = bar
     if x == 0:
          p = foo
     else:
          p = foo + bar
     while x > bar:
          p = m + n
          n = m
          m = p
          x = x + bar
     return p

def ifib__cp__cf__b(x):
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
          m = tmp
          if p == 5:
               tmp = 3 * tmp + 23  
          else: 
               tmp = tmp - 1 
          x = x-1
          tmp = tmp + 2 
     return p

