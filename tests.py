import unittest
from manejador import agregarClase, describir, dicClases

# Pruebas correspondientes a las funciones implementadas en el modulo manejador
# para ejecutar las pruebas y calcular la cobertura ejecutar el siguiente comando:
# coverage run -m unittest tests.py
# Luego se puede acceder al reporte de la cobertura con el comando
# coverage report
class Tests(unittest.TestCase):

    def test_agregarClase0(self):
        self.assertTrue(agregarClase("B",["f","g"]))

    def test_agregarClaseyaDefinida(self):
        agregarClase("A",["f","g"])
        self.assertIsNone(agregarClase("A",["h"]))
    
    def test_agregarClaseHerencia(self):
        agregarClase("c",["f","g"])
        agregarClase("d",["h"],"c")
        self.assertEqual(list(dicClases.get("d").metodos.keys()).sort(),["f","g","h"].sort())

    def test_describir_no_definida(self):
        self.assertIsNone(describir("Z"))
    
    def test_describir(self):
        agregarClase("e",["j","k"])
        self.assertEqual(describir("e"),[('j', 'e'), ('k', 'e')])

    def test_describir_con_herencia(self):
        agregarClase("h",["f","g"])
        agregarClase("i",["l","g","m"],"h")
        self.assertEqual(describir("i"),[('l', 'i'), ('g', 'i'), ('m', 'i'), ('f', 'h')])

if __name__ == '__main__':
    unittest.main()

"""
agregarClase("A",["f","g"])
describir("A")
agregarClase("B",["f","h"],"A")
print("\n")
describir("B")
agregarClase("C",["z","g"],"B")
print("\n")
describir("C")"""
