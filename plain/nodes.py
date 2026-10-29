from dataclasses import dataclass, field
from typing import Optional

# plain nodes
# by las-r

@dataclass
class Node:
    pass

# expressions
@dataclass 
class Expr(Node): 
    type: Optional[object] = field(default=None, kw_only=True)

@dataclass
class IntLit(Expr): 
    value: int

@dataclass
class FloatLit(Expr): 
    value: float

@dataclass
class BoolLit(Expr): 
    value: bool

@dataclass
class StrLit(Expr): 
    value: str

@dataclass
class UnaryOp(Expr):
    op: str
    value: Expr

@dataclass
class BinaryOp(Expr):
    left: Expr
    op: str
    right: Expr

@dataclass
class Var(Expr):
    name: str

# statements
@dataclass
class Stmt(Node): 
    pass

@dataclass
class VarDecl(Stmt):
    type_name: str
    name: str
    value: Expr

@dataclass
class VarAssign(Stmt):
    name: str
    value: Expr

@dataclass
class If(Stmt):
    cond: Expr
    body: list[Stmt]
    elsebody: list[Stmt]

@dataclass
class While(Stmt):
    cond: Expr
    body: list[Stmt]