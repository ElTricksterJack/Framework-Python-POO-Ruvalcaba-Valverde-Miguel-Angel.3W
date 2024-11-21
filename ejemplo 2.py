print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------Ejemplo 2---------------")
class Cuenta:#primero se hase la clase con sus elementos
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad
    def mostrar(self):#esta muestra el resultado en pantalla
        print(f"Usuario de la cuenta: {self.titular}")
        print(f"Dinero de cuenta: ${self.cantidad}")
ti = input("Nombre usuario de la cuenta: ")#pedir info
di = float(input("Ingrese el dinero de su cuenta: "))
print("-------------------------------")
a = Cuenta(ti, di)#mostrar info
a.mostrar()
print("-------------------------------")
rt = input("¿Desea retirar dinero de su cuenta? (si/no): ")
if rt in "si":#preguntar si quiere retirar
    rit = float(input("Ingrese la cantidad a retirar: "))
    di = di - rit#operacion
    if rit < di:#por si quedan numeros negativos
        print("--Cantidad negativa nos tendras que dever dinero--")
        c = Cuenta(ti, di)
        c.mostrar()
    else:
        print("--Gracias por retirar buelba pronto--")
        c = Cuenta(ti, di)
        c.mostrar()
else:
    print("*-*-*-*")

de = input("¿Desea retirar dinero de su cuenta? (si/no): ")
if de in "si":#preguntar si quiere depositar
    det = float(input("Ingrese la cantidad a depositar: "))
    di = di + det#operacion
    print("--Gracias por depositar buelba pronto--")
    q = Cuenta(ti, di)#mostrar
    q.mostrar()
else:
    print("--okey adios--")
print("--------------------------------------")
print("Resultado: se retiro y deposito coreptamente, tambien se vio la cuenta de ususario.\n")
