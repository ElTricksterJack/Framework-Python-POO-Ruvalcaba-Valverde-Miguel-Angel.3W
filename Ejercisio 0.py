print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------Ejemplo 0---------------")
def espal(pa):#primero hasemos una funsion.
    pa = pa.lower()#ahora la delcaramos con el lower.
    return pa == pa [::-1]#por ultimo con el return la devolvemos a "leer", por desirlo de una manera y con el -1 la leemos alrebes, y hasi se da el caso con el return lo hase true.
p = input("Escribe una palabra, palíndromo o no: ")#capturar valor.
print(espal(p))#mostrar el valor y el resultado de la funcion.
print("-------------------------------------")
print("Los palidromos son palabras que se leen igual al derecho y alrbes como ojo, ogopogo, mirim, tnt, ana, etcte.")#chiste alladido
print("Resultado: se be si la paladra es un palidromo o no.\n")
