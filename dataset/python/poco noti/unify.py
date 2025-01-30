
class V:
    def __init__(self, name):
        self.name = name

class A:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class I:
    def __repr__(self):
        return "I"
    

def f(t1, t2, subst):
    def g(t1, t2, subst):
        if isinstance(t2, V):
            if t2.name in subst:
                return g(t1, subst[t2.name], subst)
            return t1.name == t2.name
        return False
    if isinstance(t1, V):
        if t1.name in subst:
            return f(subst[t1.name], t2, subst)
        if isinstance(t2, V) and t2.name == t1.name:
            return subst
        if g(t1, t2, subst):
            raise Exception()
        subst[t1.name] = t2
        return subst
    if isinstance(t2, V):
        return f(t2, t1, subst)
    if isinstance(t1, I) and isinstance(t2, I):
        return subst
    if isinstance(t1, A) and isinstance(t2, A):
        subst = f(t1.left, t2.left, subst)
        return f(t1.right, t2.right, subst)
    raise Exception()


#########################################


class V:
    def __init__(self, name):
        self.name = name

class A:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class I:
    def __repr__(self):
        return "I"
    

def f__cp(t1, t2, subst):
    def g(t1, t2, subst):
        t3 = t2
        t4 = t1
        if isinstance(t2, V):
            if t3.name in subst:
                return g(t4, subst[t2.name], subst)
            return t4.name == t2.name
        return False
    if isinstance(t1, V):
        subst2 = subst.copy()
        subst3 = subst2
        t4 = t1
        if t1.name in subst:
            return f(subst2[t4.name], t2, subst)
        if isinstance(t2, V) and t2.name == t4.name:
            return subst
        if g(t1, t2, subst2):
            raise Exception()
        subst3[t1.name] = t2
        return subst
    if isinstance(t2, V):
        return f(t2, t1, subst)
    if isinstance(t1, I) and isinstance(t2, I):
        return subst
    if isinstance(t1, A) and isinstance(t2, A):
        subst = f(t1.left, t2.left, subst)
        return f(t1.right, t2.right, subst)
    raise Exception()