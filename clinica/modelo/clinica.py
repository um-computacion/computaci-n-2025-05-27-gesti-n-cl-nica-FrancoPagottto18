from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.turno import Turno
from modelo.receta import Receta
from modelo.historia_clinica import HistoriaClinica
from excepciones.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class Clinica:
    def __init__(self):
        self.__pacientes__ = {}
        self.__medicos__ = {}
        self.__turnos__ = []
        self.__historias_clinicas__ = {}

    def agregar_paciente(self, paciente: Paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes__:
            raise ValueError("El paciente ya está registrado.")
        self.__pacientes__[dni] = paciente
        self.__historias_clinicas__[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos__:
            raise ValueError("El médico ya está registrado.")
        self.__medicos__[matricula] = medico

    def obtener_pacientes(self):
        return list(self.__pacientes__.values())

    def obtener_medicos(self):
        return list(self.__medicos__.values())

    def obtener_medico_por_matricula(self, matricula: str):
        if matricula not in self.__medicos__:
            raise PacienteNoEncontradoException("Médico no encontrado.")
        return self.__medicos__[matricula]

    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        self.validar_turno_no_duplicado(matricula, fecha_hora)
        medico = self.__medicos__[matricula]
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)
        paciente = self.__pacientes__[dni]
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos__.append(turno)
        self.__historias_clinicas__[dni].agregar_turno(turno)

    def obtener_turnos(self):
        return list(self.__turnos__)

    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        if not medicamentos:
            raise RecetaInvalidaException("La receta debe tener al menos un medicamento.")
        paciente = self.__pacientes__[dni]
        medico = self.__medicos__[matricula]
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas__[dni].agregar_receta(receta)
        return receta

    def obtener_historia_clinica(self, dni: str):
        self.validar_existencia_paciente(dni)
        return self.__historias_clinicas__[dni]

    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes__:
            raise PacienteNoEncontradoException("Paciente no encontrado.")

    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos__:
            raise MedicoNoDisponibleException("Médico no encontrado.")

    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.__turnos__:
            if (turno.obtener_medico().obtener_matricula() == matricula and
                turno.obtener_fecha_hora() == fecha_hora):
                raise TurnoOcupadoException("El médico ya tiene un turno en ese horario.")

    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]

    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> str:
        return medico.obtener_especialidad_para_dia(dia_semana)

    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        especialidad_disponible = medico.obtener_especialidad_para_dia(dia_semana)
        if especialidad_disponible is None or especialidad_disponible != especialidad_solicitada:
            raise MedicoNoDisponibleException(
                f"El médico no atiende la especialidad '{especialidad_solicitada}' el día '{dia_semana}'."
            )
