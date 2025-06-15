import unittest
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class TestMedicoSimple(unittest.TestCase):
    def setUp(self):
        self.medico = Medico("Dr. Ana", "M12345")

    def test_agregar_especialidad_y_obtener_matricula(self):
        esp = Especialidad("Dermatología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(esp)
        self.assertEqual(self.medico.obtener_matricula(), "M12345")

    def test_obtener_especialidad_para_dia(self):
        esp = Especialidad("Dermatología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(esp)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("lunes"), "Dermatología")
        self.assertIsNone(self.medico.obtener_especialidad_para_dia("viernes"))

    def test_str(self):
        esp = Especialidad("Dermatología", ["lunes"])
        self.medico.agregar_especialidad(esp)
        esperado = "Dr. Ana, M12345, [Dermatología (Días: lunes)]"
        self.assertEqual(str(self.medico), esperado)

    def test_str_sin_especialidades(self):
        esperado = "Dr. Ana, M12345, [Sin especialidades]"
        self.assertEqual(str(self.medico), esperado)

    def test_str_varias_especialidades(self):
        esp1 = Especialidad("Dermatología", ["lunes"])
        esp2 = Especialidad("Cardiología", ["martes"])
        self.medico.agregar_especialidad(esp1)
        self.medico.agregar_especialidad(esp2)
        esperado = "Dr. Ana, M12345, [Dermatología (Días: lunes), Cardiología (Días: martes)]"
        self.assertEqual(str(self.medico), esperado)

if __name__ == "__main__":
    unittest.main()
