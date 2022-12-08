"""1. Definir una funcion max() que tome como argumento dos numeros y 
    devuelva el mayor de ellos.
    (Es cierto que python ya tiene una funcion max() incorporada,
    pero hacerla nosotros mismos es muy buen ejericio)
    """

'''consejo 1: siempre colocar un docstring'''
'''consejo 2: realizar 2 pruebas minimo'''
'''consejo 3: preguntar lo que se retorne o es una excepcion y crear una excepcion en la que 
no se pueda devolver el valor en caso de que ambos numeros sean iguales'''

from calendar import c


def custom_max(n1:int, n2:int):
    """dado dos numeros de entrada retorna el maximo de ambos

    Args:
        n1 (int): Primer numero a comparar
        n2 (int): Segundo numero a comparar

    Returns:
        int: mayor de ambos
    """
    if n2 > n1:
        return n2
    elif n1 > n2: 
        return n1
    elif n1 == n2:
        raise Exception("Los valores no pueden ser iguales")
    raise Exception("Algo ha salido mal")

# probar la funcion
print(custom_max(1,2))
print(custom_max(3,2))
print(custom_max(3,3))



"""Definir una función max_de_tres(), que tome tres números como argumentos
y devuelva el mayor de ellos."""

def max_de_tres(n1:int, n2:int, n3:int):
    """Toma 3 numeros como argumentos y devulve el mayor de ellos.

    Args:
        n1 (int): primer numero a comparar
        n2 (int): segundo numero a comparar
        n3 (int): tercer numero a comparar
    
    Returns:
        int: Mayor de los tres numeros
    """
    """
    explicar la propiedad transitiva de este paradigma suma mucho en la entrevista
    a > b > c
    b > c
    a > c
    """
    
    n = custom_max(n1, n2)
    n_final = custom_max(n3, n)
    return n_final
# solo falta anexar la excepcion en caso de ser iguales

# probando la funcion
print(max_de_tres(1,2,5))