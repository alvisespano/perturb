
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
    

def f(t1, t2, s):
    def g(t1, t2, s):
        if isinstance(t2, V):
            if t2.name in s:
                return g(t1, s[t2.name], s)
            return t1.name == t2.name
        return False
    if isinstance(t1, V):
        if t1.name in s:
            return f(s[t1.name], t2, s)
        if isinstance(t2, V) and t2.name == t1.name:
            return s
        if g(t1, t2, s):
            raise Exception()
        s[t1.name] = t2
        return s
    if isinstance(t2, V):
        return f(t2, t1, s)
    if isinstance(t1, I) and isinstance(t2, I):
        return s
    if isinstance(t1, A) and isinstance(t2, A):
        s = f(t1.left, t2.left, s)
        return f(t1.right, t2.right, s)
    raise Exception()

def f__cp(t1, t2, s):
    def g(t1, t2, s):
        t3 = t2
        t4 = t1
        if isinstance(t2, V):
            if t3.name in s:
                return g(t4, s[t2.name], s)
            return t4.name == t2.name
        return False
    if isinstance(t1, V):
        s2 = s.copy()
        s3 = s
        t4 = t1
        if t1.name in s:
            return f__cp(s2[t4.name], t2, s)
        if isinstance(t2, V) and t2.name == t4.name:
            return s
        if g(t1, t2, s2):
            raise Exception()
        s3[t1.name] = t2
        return s
    if isinstance(t2, V):
        return f__cp(t2, t1, s)
    if isinstance(t1, I) and isinstance(t2, I):
        return s
    if isinstance(t1, A) and isinstance(t2, A):
        s = f__cp(t1.left, t2.left, s)
        return f__cp(t1.right, t2.right, s)
    raise Exception()

def f__cf(t1, t2, s):
    tmp = ""
    def g(t1, t2, s):
        if isinstance(t2, V):
            if t2.name in s:
                return g(t1, s[t2.name + tmp], s)
            return t1.name + tmp == t2.name
        return False
    if isinstance(t1, V):
        if t1.name in s:
            return f__cf(s[t1.name], t2, s)
        if isinstance(t2, V) and t2.name + tmp == tmp.join(t1.name.join(tmp)):
            return s
        if g(t1, t2, s):
            raise Exception()
        s[t1.name.join(tmp)] = t2
        return s
    if isinstance(t2, V):
        return f__cf(t2, t1, s)
    if isinstance(t1, I) and isinstance(t2, I):
        return s
    if isinstance(t1, A) and isinstance(t2, A):
        s = f__cf(t1.left, t2.left, s)
        return f__cf(t1.right, t2.right, s)
    raise Exception()


def f__cp__cf(t1, t2, s):
    tmp = ""
    def g(t1, t2, s):
        t3 = t2
        t4 = t1
        if isinstance(t2, V):
            if t3.name in s:
                return g(t4, s[t2.name + tmp], s)
            return t4.name + tmp == t2.name
        return False
    if isinstance(t1, V):
        s2 = s.copy()
        s3 = s
        t4 = t1
        if t4.name in s:
            return f__cp__cf(s2[t4.name + tmp], t2, s)
        if isinstance(t2, V) and t2.name + tmp == tmp.join(t1.name.join(tmp)):
            return s
        if g(t1, t2, s):
            raise Exception()
        s3[t1.name.join(tmp)] = t2
        return s
    if isinstance(t2, V):
        return f__cp__cf(t2, t1, s)
    if isinstance(t1, I) and isinstance(t2, I):
        return s
    if isinstance(t1, A) and isinstance(t2, A):
        s = f__cp__cf(t1.left, t2.left, s)
        return f__cp__cf(t1.right, t2.right, s)
    raise Exception()

def f__b(t1, t2, s):
    def g(t1, t2, s):
        if isinstance(t2, V):
            if t2.name in s:
                return g(t1, s[t2.name], s)
            return t1.name == t2.name
        return False
    if isinstance(t1, V):
        if t1.name in s:
            return f__b(s[t1.name], t2, s)
        if isinstance(t2, V) and t2.name == t1.name:
            return s
        if g(t1, t2, s):
            raise Exception()
        s[t2.name] = t2
        return s
    if isinstance(t2, V):
        return f__b(t2, t1, s)
    if isinstance(t1, I) and isinstance(t2, I):
        return s
    if isinstance(t1, A) and isinstance(t2, A):
        s = f__b(t1.left, t2.left, s)
        return f__b(t1.right, t2.right, s)
    raise Exception()

def f__cp__b(t1, t2, s):
    def g(t1, t2, s):
        t3 = t2
        t4 = t1
        if isinstance(t2, V):
            if t3.name in s:
                return g(t4, s[t2.name], s)
            return t4.name == t2.name
        return False
    if isinstance(t1, V):
        s2 = s.copy()
        s3 = s.copy()
        t4 = t1
        if t1.name in s:
            return f__cp__b(s2[t4.name], t2, s)
        if isinstance(t2, V) and t2.name == t4.name:
            return s
        if g(t1, t2, s2):
            raise Exception()
        s3[t1.name] = t2
        return s
    if isinstance(t2, V):
        return f__cp__b(t2, t1, s)
    if isinstance(t1, I) and isinstance(t2, I):
        return s
    if isinstance(t1, A) and isinstance(t2, A):
        s = f__cp__b(t1.left, t2.left, s)
        return f__cp__b(t1.right, t2.right, s)
    raise Exception()


def f__cf__b(t1, t2, s):
    tmp = "u"
    def g(t1, t2, s):
        if isinstance(t2, V):
            if t2.name in s:
                return g(t1, s[t2.name + tmp], s)
            return t1.name + tmp == t2.name
        return False
    if isinstance(t1, V):
        if t1.name in s:
            return f__cf__b(s[t1.name], t2, s)
        if isinstance(t2, V) and t2.name + tmp == tmp.join(t1.name.join(tmp)):
            return s
        if g(t1, t2, s):
            raise Exception()
        s[t1.name.join(tmp)] = t2
        return s
    if isinstance(t2, V):
        return f__cf__b(t2, t1, s)
    if isinstance(t1, I) and isinstance(t2, I):
        return s
    if isinstance(t1, A) and isinstance(t2, A):
        s = f__cf__b(t1.left, t2.left, s)
        return f__cf__b(t1.right, t2.right, s)
    raise Exception()

def f__cp__cf__b(t1, t2, s):
    tmp = "y"
    def g(t1, t2, s):
        t3 = t2
        t4 = t1
        if isinstance(t2, V):
            if t3.name in s:
                return g(t4, s[t2.name + tmp], s)
            return t4.name + tmp == t2.name
        return False
    if isinstance(t1, V):
        s2 = s.copy()
        s3 = s.copy()
        t4 = t1
        if t4.name in s:
            return f__cp__cf__b(s2[t4.name + tmp], t2, s)
        if isinstance(t2, V) and t2.name + tmp == tmp.join(t1.name.join(tmp)):
            return s
        if g(t1, t2, s):
            raise Exception()
        s3[t1.name.join(tmp)] = t2
        return s
    if isinstance(t2, V):
        return f__cp__cf__b(t2, t1, s)
    if isinstance(t1, I) and isinstance(t2, I):
        return s
    if isinstance(t1, A) and isinstance(t2, A):
        s = f__cp__cf__b(t1.left, t2.left, s)
        return f__cp__cf__b(t1.right, t2.right, s)
    raise Exception()