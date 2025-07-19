#funcion calculadora 
def sumar(a: float, b: float) -> float:
    #Suma dos números.
    return a + b

def restar (a: float, b: float) -> float:
    #Resta el segundo número al primero.
    return a - b

def multiplicar(a: float, b: float) -> float:
    #Multiplica dos números.
    return a * b

def dividir(a: float, b: float) -> float:
   #Divide el primer número por el segundo.
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def potencia(a: float, b: float) -> float:
   # Calcula a elevado a la b.
    return a**b


if __name__ == "__main__":
    print(sumar(9, 6))         
    print(restar(11, 9))         
    print(multiplicar(9, 9))    
    print(dividir(20, 2))       

