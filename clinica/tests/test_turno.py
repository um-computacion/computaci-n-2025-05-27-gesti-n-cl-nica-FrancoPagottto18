import unittest
from datetime import datetime
from modelo.turno import Turno
from modelo.paciente import Paciente
from modelo.medico import Medico

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dra. Lopez", "M9876")
        self.fecha_hora = datetime(2025, 6, 10, 14, 30)
        self.especialidad = "Cardiología"
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora, self.especialidad)

    def test_accesos(self):
        self.assertEqual(self.turno.obtener_medico(), self.medico)
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)

    def test_str(self):
        esperado = (f"Turno: Paciente: {self.paciente}, Médico: {self.medico}, "
                    f"Especialidad: {self.especialidad}, Fecha y hora: 10/06/2025 14:30")
        self.assertEqual(str(self.turno), esperado)

if __name__ == "__main__":
    unittest.main()
