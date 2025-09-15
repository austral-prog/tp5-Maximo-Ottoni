def roots(a, b, c):
    import math  # Importa el módulo math para usar funciones matemáticas como sqrt()
    
    discriminant = b ** 2 - 4 * a * c  # Calcula el discriminante b^2 - 4ac
    
    if discriminant > 0:  # Si el discriminante es mayor a 0 → dos raíces reales distintas
        r1 = (-b + math.sqrt(discriminant)) / (2 * a)  # Calcula la primera raíz
        r2 = (-b - math.sqrt(discriminant)) / (2 * a)  # Calcula la segunda raíz
        return f"({r1}, {r2})"  # Devuelve las dos raíces como string
    
    elif discriminant == 0:  # Si el discriminante es 0 → una raíz doble
        r = -b / (2 * a)  # Calcula la raíz
        return f"({r})"  # Devuelve la raíz única como string
    
    else:  # Si el discriminante es negativo → no hay raíces reales
        return "( )"  # Devuelve un string vacío


def value_y(a, b, c, x):
    return a * x ** 2 + b * x + c  # Calcula el valor de y para un x dado en la ecuación cuadrática


def to_string(a, b, c):
    terms = []  # Lista donde se guardan los términos que no son 0
    
    if a != 0:
        terms.append(f"{a} * X^2")  # Si a no es 0, agrega el término ax^2
    
    if b != 0:
        terms.append(f"{b} * X")  # Si b no es 0, agrega el término bx
    
    if c != 0 or (a == 0 and b == 0):
        terms.append(f"{c}")  # Si c no es 0 o si a y b son 0, agrega c
    
    return "f(x) = " + " + ".join(terms)  # Une todos los términos con " + " y devuelve la ecuación


def derivation(a, b, c):
    da = 2 * a  # Coeficiente de x en la derivada (d/dx[ax^2] = 2ax)
    db = b      # Coeficiente constante en la derivada (d/dx[bx] = b)
    
    if da != 0 and db != 0:
        return f"f'(x) = {da} * X + {db}"  # Si ambos son distintos de 0, devuelve derivada completa
    elif da != 0:
        return f"f'(x) = {da} * X"  # Si solo da no es 0, devuelve f'(x) = 2a * X
    else:
        return f"f'(x) = {db}"  # Si da = 0, devuelve f'(x) = b
    # Si ambos son 0, devuelve f'(x) = 0