import unittest
from modelo.paciente import Paciente

class TestPaciente(unittest.TestCase):

    def test_obtener_dni(self):
        paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.assertEqual(paciente.obtener_dni(), "12345678")

    def test_str(self):
        paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.assertEqual(str(paciente), "Juan Pérez, 12345678, 12/12/2000")

if __name__ == "__main__":
    unittest.main()
