from typing import Dict, Union

Ty = Union['TyVar', 'TyInt', 'TyArrow']

class TyVar:
    def __init__(self, name: str):
        self.name = name

class TyArrow:
    def __init__(self, left: Ty, right: Ty):
        self.left = left
        self.right = right

class TyInt:
    def __repr__(self):
        return "int"
    
Subst = Dict[str, Ty]

def unify(t1: Ty, t2: Ty, subst: Subst) -> Subst:
    def occurs_check(t1: Ty, t2: Ty, subst: Subst) -> bool:
        if isinstance(t2, TyVar):
            if t2.name in subst:
                return occurs_check(t1, subst[t2.name], subst)
            return t1.name == t2.name
        return False
    if isinstance(t1, TyVar):
        if t1.name in subst:
            return unify(subst[t1.name], t2, subst)
        if isinstance(t2, TyVar) and t2.name == t1.name:
            return subst
        if occurs_check(t1, t2, subst):
            raise TypeError(f"Recursive type: {t1} occurs in {t2}")
        subst[t1.name] = t2
        return subst
    if isinstance(t2, TyVar):
        return unify(t2, t1, subst)
    if isinstance(t1, TyInt) and isinstance(t2, TyInt):
        return subst
    if isinstance(t1, TyArrow) and isinstance(t2, TyArrow):
        subst = unify(t1.left, t2.left, subst)
        return unify(t1.right, t2.right, subst)

    raise TypeError(f"Type mismatch: {t1} != {t2}")
