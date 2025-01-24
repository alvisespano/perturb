from typing import Dict, Union

Type = Union['TypeVar', 'IntType']

class TypeVar:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

class IntType:
    def __repr__(self):
        return "int"

INT_TYPE = IntType()

#####################

Expr = Union['Var', 'Abs', 'App', 'Let']

class Var:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name

class Abs:
    def __init__(self, var: str, body: Expr):
        self.var = var
        self.body = body

    def __repr__(self):
        return f"λ{self.var}. {self.body}"

class App:
    def __init__(self, func: Expr, arg: Expr):
        self.func = func
        self.arg = arg

    def __repr__(self):
        return f"({self.func} {self.arg})"

class Let:
    def __init__(self, var: str, expr: Expr, body: Expr):
        self.var = var
        self.expr = expr
        self.body = body

    def __repr__(self):
        return f"let {self.var} = {self.expr} in {self.body}"

TypeEnv = Dict[str, Type]

#####################

fresh_tyvar_counter = 0

def fresh() -> TypeVar:
    global fresh_tyvar_counter
    fresh_tyvar_counter += 1
    return TypeVar(f"t{fresh_tyvar_counter}")

def unify(t1: Type, t2: Type, subst: Dict[str, Type]) -> Dict[str, Type]:
    if isinstance(t1, TypeVar):
        if t1.name in subst:
            return unify(subst[t1.name], t2, subst)
        if isinstance(t2, TypeVar) and t2.name == t1.name:
            return subst
        if occurs_check(t1, t2, subst):
            raise TypeError(f"Recursive type: {t1} occurs in {t2}")
        subst[t1.name] = t2
        return subst
    if isinstance(t2, TypeVar):
        return unify(t2, t1, subst)
    if isinstance(t1, IntType) and isinstance(t2, IntType):
        return subst
    raise TypeError(f"Type mismatch: {t1} != {t2}")

def occurs_check(t1: TypeVar, t2: Type, subst: Dict[str, Type]) -> bool:
    if isinstance(t2, TypeVar):
        if t2.name in subst:
            return occurs_check(t1, subst[t2.name], subst)
        return t1.name == t2.name
    return False

def infer(env: TypeEnv, e: Expr, subst: Dict[str, Type]) -> tuple[Type, Dict[str, Type]]:
    if isinstance(e, Var):
        ty = env.get(e.name)
        if ty is None:
            raise TypeError(f"Unbound variable: {e.name}")
        return ty, subst
    elif isinstance(e, Abs):
        ty_var = fresh()
        new_env = env.copy()
        new_env[e.var] = ty_var
        body_ty, subst = infer(new_env, e.body, subst)
        return ty_var, subst
    elif isinstance(e, App):
        func_ty, subst = infer(env, e.func, subst)
        arg_ty, subst = infer(env, e.arg, subst)
        res_ty = fresh()
        subst = unify(func_ty, arg_ty, subst)
        return res_ty, subst
    elif isinstance(e, Let):
        expr_ty, subst = infer(env, e.expr, subst)
        new_env = env.copy()
        new_env[e.var] = expr_ty
        body_ty, subst = infer(new_env, e.body, subst)
        return body_ty, subst
    else:
        raise TypeError(f"Unknown expression: {e}")
