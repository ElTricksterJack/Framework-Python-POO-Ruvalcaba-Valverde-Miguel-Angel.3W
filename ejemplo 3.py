print("\nRuvalcaba Valverde Miguel Angel_1212_3W")
print("---------------Ejemplo 3---------------")

class CuentaJoven:#creamos una clase con 4 objetos
    def __init__(self, titulo, cantidad, bonificacion, edad):
        self.titulo = titulo
        self.cantidad = cantidad
        self.bonificacion = bonificacion
        self.edad = edad

    def creacu(self):#aremos una funcion para crear un cuenta
        if self.edad > 24:#esta parte denimina que apartir del valor dado sera balido o no haser tu cuenta.
            print("/--Aplicas para crear una cuenta--/")#estos de abajo capturan la info para cuenta
            self.titulo = input("Ingresa tu nombre de usuario: ")
            self.cantidad = float(input("Ingresa tu dinero: $"))
            self.bonificacion = float(input("Ingresa tu bonificación: %"))
            print(f"-Cuenta de {self.titulo}-\nDeposito: ${self.cantidad}\nBonificación: {self.bonificacion}%")#muestra los datos
            print("7-7-7")
            it = input("¿Quieres ver el extra de tu bonificación? (si/no): ")#ahora podemos ver si queremos el extra que nos da la bonificacion
            if it == "si":
                extra = self.cantidad * self.bonificacion / 100#aqui se hasen las operaciones esta---es para calcular e extra
                to = self.cantidad + extra#esta es para calcular el total
                print(f"Tu bonificación es de {self.bonificacion}%")#se muestra la bonificacion, el extra y el total
                print(f"Extra de tu bonificación: ${extra}")
                print(f"Total: ${to}")
            else:#opcion si no quieres ver tu bonificacion
                print("|Okey|")
        else:#mensaje por si no tienes 25 o mas
            print("No puedes crear una cuenta")

ed = int(input("Ingresa tu edad: "))#ingresar la edad del usuario
wk = CuentaJoven("", 0, 0, ed)#Nota: esta parte fue el mallor dolor de cabeza, hasi que busque alludia y era por el orden-Recuerda yo el orden es importante.
wk.creacu()

print("--------------------------------------")
print("Resultado: se logro ver todo coreptamente.\n")
