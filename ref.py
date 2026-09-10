# Abstract Base Class import (necessária para a implementação de interfaces)
from abc import ABC

# Definição de uma classe:
class MinhaClasseFilha(MinhaClassePai, MinhaClasseMae):
    pass

# Encapsulamento de Atributos Protegidos (1 subtraço)
self._meuAtributoProtegido = 0

# Encapsulamento de Atributos Privados (2 subtraços)
self.__meuAtributoPrivado = 0

# Instanciamento manual (executado ANTES de __init__)
def __new__(cls, *args, **kwargs):
    pass

# Construtor com Valores Padrão:
def __init__(self):
    pass

# Destrutor
def __del__(self):
    # del(self)
    pass

# uso de super:
super().__init__()
MinhaClassePai.__init__()
MinhaClasseMae.__init__()

# Decoradores para getter:
@property
def myAttributeName(self):
    pass

# Decoradores para setter:
@myAttributeName.setter
def myAttributeName(self):
    pass

# Atributo de classe:
meuAtributoCompartilhado = 0

# Método de Classe:
@classmethod
def meuMetodoObrigatorio (cls):
    pass

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








# Checagem de tipo e hierarquia
isinstance(minhaInstancia, MinhaClasse)
issubclass(ClasseFilha, ClassePai)

# Tratamento de erros:
try:
    pass
except Exception as e:
    pass

# disparar exceção
raise Error

# Principais exceções:
TypeError
ValueError
NameError
ZeroDivisionError
FileNotFoundError
IndexError
KeyError

