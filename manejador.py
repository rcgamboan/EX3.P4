
class Clase:
    def __init__(self,nombre,metodos,super=None):
        self.nombre = nombre
        self.super = super
        self.metodos = metodos

dicClases = {}

def agregarClase(nombre,metodos,super=None) :

    if dicClases.get(nombre) != None:
        print(f"La clase {nombre} ya se encuentra definida")
        return

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
            return
    dicClases[nombre] = Clase(nombre,methods,super)

def describir(nombre):
    clase = dicClases.get(nombre)
    if clase == None:
        print(f"La clase {nombre} no se encuentra definida")
        return

    for metodo in clase.metodos.keys():
        print(f"{metodo} -> {clase.metodos.get(metodo)} :: {metodo}")
"""
agregarClase("A",["f","g"])
describir("A")
agregarClase("B",["f","h"],"A")
print("\n")
describir("B")
agregarClase("C",["z","g"],"B")
print("\n")
describir("C")"""
