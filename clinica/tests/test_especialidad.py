import unittest
from modelo.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def test_creacion_basica(self):
        esp = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.assertEqual(esp.obtener_especialidad(), "Pediatría")
        self.assertEqual(esp.__str__(), "Pediatría (Días: lunes, miércoles)")

    def test_verificar_dia(self):
        esp = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.assertTrue(esp.verificar_dia("lunes"))
        self.assertTrue(esp.verificar_dia("LUNES")) 
        self.assertFalse(esp.verificar_dia("viernes"))

if __name__ == "__main__":
    unittest.main()