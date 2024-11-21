print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------Ejemplo 1---------------")
class persona:#primero agamos una clase con barios elementos de una DNI.
    def __init__(self, name, edad, ci, ln, ni, se, cor):
        self.name = name
        self.edad = edad
        self.ci = ci
        self.ln = ln
        self.ni = ni
        self.se = se
        self.cor = cor
    def mos(self):#esta imprime el mensaje
        print(f"Nombre: {self.name}__Edad: {self.edad} -+-Estado civil: {self.ci}/Lugar de nacimiento: {self.ln}/Numero de identificacion: {self.ni} -+-Sexo: {self.se} * Coreo electronico: {self.cor}")
na = input("ingresa tu nombre: ")#esto captura los datos.
ed = input("ingresa tu edad: ")
ci = input("ingresa tu Estado civil: ")
ln = input("ingresa tu Lugar de nacimiento: ")
ni = input("ingresa tu Numero de identificacion: ")
se = input("ingresa tu Sexo: ")
cor = input("ingresa tu Correo electronico: ")
inte=persona(na,ed,ci,ln,ni,se,cor)#ahora a invocar la funsion y clase.
inte.mos()

print("-------------------------------------")
print("Resultado: se be el mensaje bien y con los datos agregados.\n")
