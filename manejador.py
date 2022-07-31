# Pregunta 4, Examen 3 CI3641.
# Elaborado por Roberto Gamboa, 16-10394

# implementacion de un manejador de tablas de métodos virtuales 
# para un sistema orientado a objetos con herencia simple y despacho
# dinámico de métodos



# Clase que representa una nueva clase a agregar
# contiene el nombre de la clase, la superclase de la que hereda (si aplica, caso contrario es None)
# y un diccionario cuyas claves son los nombres de los metodos que contiene y los que hereda de su superclase
class Clase:
    def __init__(self,nombre,metodos,super=None):
        self.nombre = nombre
        self.super = super
        self.metodos = metodos

# Diccionario que almacena todas las clases creadas
# sus claves son los nombres de las clases
# y sus valores son los objetos tipo Clases correspondientes
dicClases = {}

# metodo que agrega crea una nueva clase con el nombre, metodos y superclase suministrados
# Si ya existe una clase asociada al nombre dado, se reporta un error
# Si la superclase dada no existe reporta un error
# en caso de que la superclase no sea None, se agregan los metodos de la superclase
# y los metodos dados como argumento a la nueva clase
# si algun metodo de la superclase se redefine en la clase actual, se agrega el de la clase actual
def agregarClase(nombre,metodos,super=None) :

    if dicClases.get(nombre) != None:
        print(f"La clase {nombre} ya se encuentra definida")
        return None

    methods = {}

    for metodo in metodos:
        methods[metodo] = nombre
    
    if super != None:
        superclase = dicClases.get(super)
        if superclase != None:
            for metodo in superclase.metodos.keys():
                if methods.get(metodo) == None:
                    methods[metodo] = superclase.metodos.get(metodo)
        else:
            print("la superclase especificada no existe")
            return None
    dicClases[nombre] = Clase(nombre,methods,super)
    return True

# metodo que describe la clase asociada al nombre suministrado
# recibe el nombre de la clase que se quiere describir
# verifica que la clase exista y muestra sus metodos
def describir(nombre):
    clase = dicClases.get(nombre)
    if clase == None:
        print(f"La clase {nombre} no se encuentra definida")
        return None
    mets = []
    for metodo in clase.metodos.keys():
        print(f"{metodo} -> {clase.metodos.get(metodo)} :: {metodo}")
        mets.append((metodo,clase.metodos.get(metodo)))
    return mets
