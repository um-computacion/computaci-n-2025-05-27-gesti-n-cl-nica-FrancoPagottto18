from datetime import datetime

class Turno:
    def __init__(self, paciente, medico, fecha_hora: datetime, especialidad: str):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__fecha_hora__ = fecha_hora
        self.__especialidad__ = especialidad

    def obtener_medico(self):
        return self.__medico__

    def obtener_fecha_hora(self):
        return self.__fecha_hora__

    def __str__(self):
        return (f"Turno: Paciente: {self.__paciente__}, "
                f"Médico: {self.__medico__}, "
                f"Especialidad: {self.__especialidad__}, "
                f"Fecha y hora: {self.__fecha_hora__.strftime('%d/%m/%Y %H:%M')}")
