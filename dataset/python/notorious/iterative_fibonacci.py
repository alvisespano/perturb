
def f(x):
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

def f__cp(x):
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


def f__cf(x):
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

def f__cp__cf(x):
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
          x = x - 1
          tmp = tmp + 2 
     return p

def f__b(x):
     n = 0
     m = 1
     if x == 0:
          p = 0
     else:
          p = 1
     while x > 1:
          p = m + n
          n = m
          m = n
          x = x - 1
     return p

def f__cp__b(x):
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

def f__cf__b(x):
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

def f__cp__cf__b(x):
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
          x = x - 1
          tmp = tmp + 2 
     return p

###################################################
###################################################
###################################################
###################################################

import random

def test_functions(funcs, test_cases):
    for i, test_case in enumerate(test_cases):
        expected = funcs[0](test_case)
        print(f"Test case {i + 1}: {test_case}")
        for func in funcs:
            result = func(test_case)
            if result != expected:
                print(f"\t❌ {func.__name__} produced {result}, expected {expected}")
            else:
                print(f"\t✅ {func.__name__} successful")

functions = [
    f, f__cp, f__cf, f__cp__cf, 
    f__b, f__cp__b, f__cf__b, f__cp__cf__b
]

test_cases = [
    0, 1, 2, 3, 4, 5, 
    random.randint(6, 15), random.randint(15, 30)
]

test_functions(functions, test_cases)
