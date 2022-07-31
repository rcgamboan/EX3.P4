import sys
import manejador

# cliente que usa las funciones definidas en manejador
# para simular un manejador de tablas de métodos virtuales 

print("\n\nManejador de tipos de datos")
print("\nA continuacion indique la operacion que quiere realizar")
print("\nLas operaciones disponibles son las siguientes: ")
print("\nCLASS     <tipo> [<nombre>] Deﬁne un nuevo tipo que poseerá métodos con nombres establecidos en la lista ")
print("\nDESCRIBIR <nombre> Muestra la tabla de métodos virtuales para el tipo con el nombre propuesto.")
print("\nSALIR     Termina la ejecucion del programa\n")
while True:

    comando = input("main> ")

    if comando == '':
        continue

    argumentos = comando.split()

    if argumentos[0] == "SALIR" or argumentos[0] == "salir":
        print("Se termina la ejecucion del programa")
        sys.exit()
    elif argumentos[0] == "CLASS":
        
        if len(argumentos) < 3:
            print("Formato invalido.")
        else:
            nombre = argumentos[1]
            if argumentos[2] == ':':
                super = argumentos[3]
                tipos = argumentos[4:]
                manejador.agregarClase(nombre,tipos,super)
            else:
                tipos = argumentos[2:]
                manejador.agregarClase(nombre,tipos)  

    
    elif argumentos[0] == "DESCRIBIR":

        if len(argumentos) != 2:
            print("Formato invalido.")
        else:
            nombre = argumentos[1]
            manejador.describir(nombre)
                
            
    else:
        print("Operacion no valida\n")

