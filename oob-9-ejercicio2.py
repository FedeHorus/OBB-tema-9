
from functools import reduce


def impares(elementos):
    resultado = list(filter(lambda x : x % 2, elementos))
    print(f'funcion Filter', resultado)
    
    resultado = reduce((lambda a,b: a+b), elementos)
    print('Funcion reduce ',resultado)
    
    
def __str__(impares):
    return impares


elementos = list(range(200))
impares(elementos)
