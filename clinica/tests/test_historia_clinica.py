import unittest
from modelo.historia_clinica import HistoriaClinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.turno import Turno
from modelo.receta import Receta
from datetime import datetime

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.historia = HistoriaClinica(self.paciente)
        self.medico = Medico("Dra. Lopez", "M9876")
        self.turno = Turno(self.paciente, self.medico, datetime(2025, 6, 10, 14, 30), "Cardiología")
        self.receta = Receta(self.paciente, self.medico, ["Paracetamol"])

    def test_agregar_y_obtener(self):
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        self.assertIn(self.turno, self.historia.obtener_turnos())
        self.assertIn(self.receta, self.historia.obtener_recetas())

    def test_str(self):
        texto = str(self.historia)
        self.assertIn("Historia clínica de: Juan Perez, 12345678, 01/01/1990", texto)
        self.assertIn("(Sin turnos)", texto)
        self.assertIn("(Sin recetas)", texto)
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        texto2 = str(self.historia)
        self.assertIn("- Turno: Paciente: Juan Perez, 12345678, 01/01/1990", texto2)
        self.assertIn("- Receta para: Juan Perez, 12345678, 01/01/1990", texto2)

if __name__ == "__main__":
    unittest.main()
