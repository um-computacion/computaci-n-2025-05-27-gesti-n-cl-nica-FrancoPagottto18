import unittest
from datetime import datetime
from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from excepciones.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Perez", "12345678", "01/01/1990")
        self.medico = Medico("Dra. Lopez", "M9876")
        self.especialidad = Especialidad("Cardiología", ["lunes"])
        self.medico.agregar_especialidad(self.especialidad)
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agregar_paciente_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_paciente(self.paciente)

    def test_agregar_medico_duplicado(self):
        with self.assertRaises(ValueError):
            self.clinica.agregar_medico(self.medico)

    def test_agendar_turno_ok(self):
        fecha = datetime(2025, 6, 9, 10, 0)  
        self.clinica.agendar_turno("12345678", "M9876", "Cardiología", fecha)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_agendar_turno_paciente_inexistente(self):
        fecha = datetime(2025, 6, 9, 10, 0)
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "M9876", "Cardiología", fecha)

    def test_agendar_turno_medico_inexistente(self):
        fecha = datetime(2025, 6, 9, 10, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M0000", "Cardiología", fecha)

    def test_agendar_turno_duplicado(self):
        fecha = datetime(2025, 6, 9, 10, 0)
        self.clinica.agendar_turno("12345678", "M9876", "Cardiología", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("12345678", "M9876", "Cardiología", fecha)

    def test_agendar_turno_especialidad_incorrecta(self):
        fecha = datetime(2025, 6, 9, 10, 0)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "M9876", "Pediatría", fecha)

    def test_emitir_receta_ok(self):
        receta = self.clinica.emitir_receta("12345678", "M9876", ["Paracetamol"])
        self.assertIn("Paracetamol", str(receta))

    def test_emitir_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "M9876", [])

    def test_obtener_historia_clinica(self):
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertIn("Historia clínica de: Juan Perez", str(historia))

if __name__ == "__main__":
    unittest.main()
