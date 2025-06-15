import unittest
from modelo.receta import Receta
from modelo.paciente import Paciente
from modelo.medico import Medico
from datetime import datetime

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dra. Lopez", "M9876")
        self.medicamentos = ["Paracetamol", "Ibuprofeno"]
        self.receta = Receta(self.paciente, self.medico, self.medicamentos)

    def test_str(self):
        resultado = str(self.receta)
        self.assertIn("Receta para: Juan Perez, 12345678, 01/01/1990", resultado)
        self.assertIn("Médico: Dra. Lopez, M9876, [Sin especialidades]", resultado)
        self.assertIn("Medicamentos: Paracetamol, Ibuprofeno", resultado)
        self.assertIn("Fecha de emisión:", resultado)

if __name__ == "__main__":
    unittest.main()
