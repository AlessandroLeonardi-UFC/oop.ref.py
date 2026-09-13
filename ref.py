#### Guia de Referência Rápida para a AP01 - POO ####


# Definição de uma classe:
class MinhaClasse:
    pass

# Encapsulamento de Atributos Protegidos (1 subtraço)
self._meuAtributoProtegido = 0

# Encapsulamento de Atributos Privados (2 subtraços)
self.__meuAtributoPrivado = 0

# Construtor com Valores Padrão:
def __init__(self):
    pass

# Destrutor
def __del__(self):
    # del(self)
    pass
    
# Decoradores para getter:
@property
def meuAtributo(self):
    pass

# Decoradores para setter:
@meuAtributo.setter
def meuAtributo(self):
    pass


















## Página 01
# Double Underscore Methods (Dundle) para sobrecarga de operadores:
def __str__(self):
    # print(f"{self}")
    pass

def __len__(self):
    # len(self)
    pass

def __pos__(self): 
    # +p1
    pass

def __neg__(self):
    # -p1
    pass

def __add__(self, other):
    # p1 + p2
    pass

def __sub__(self, other):
    # p1 - p2
    pass

def __mul__(self, other):
    # p1 - p2
    pass

def __pow__(self, other):
    # p1 ** p2
    pass

def __truediv__(self, other):
    # p1 / p2
    pass

def __floordiv__(self, other):
    # p1 // p2
    pass

def __mod__(self, other):
    # p1 % p2
    pass

def __invert__(self):
    # ~p1
    pass

# Página 02
def __lt__(self, other):
    # p1 < p2
    pass

def __gt__(self, other):
    # p1 > p2
    pass

def __le__(self, other):
    # p1 <= p2
    pass

def __ge__(self, other):
    # p1 >= p2
    pass

def __eq__(self, other):
    # p1 == p2
    pass

def __ne__(self, other):
    # p1 != p2
    pass

def __lshift__(self, other):
    # p1 << p2
    pass

def __rshift__(self, other):
    # p1 >> p2
    pass

def __and__(self, other):
    # p1 & p2
    pass

def __or__(self, other):
    # p1 | p2
    pass

def __xor__(self, other):
    # p1 ^ p2
    pass






# Página 03
# Checagem de tipo
isinstance(valorQueroVerificar, TipoQueDeveSer )

# Tratamento de erros:
try:
    pass
except Exception as e:
    pass

# disparar exceção
raise Error("Mensagem")

# Principais exceções:
TypeError
ValueError
NameError
RuntimeError
ZeroDivisionError
FileNotFoundError
IndexError
KeyError




























# Página 04
