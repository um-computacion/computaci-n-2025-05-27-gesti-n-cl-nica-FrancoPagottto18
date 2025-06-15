from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos: list[str]):
        self.__paciente__ = paciente
        self.__medico__ = medico
        self.__medicamentos__ = medicamentos
        self.__fecha__ = datetime.now()

    def __str__(self):
        meds = ", ".join(self.__medicamentos__)
        return (f"Receta para: {self.__paciente__}\n"
                f"Médico: {self.__medico__}\n"
                f"Medicamentos: {meds}\n"
                f"Fecha de emisión: {self.__fecha__.strftime('%d/%m/%Y %H:%M')}")
