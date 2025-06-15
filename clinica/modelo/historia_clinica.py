class HistoriaClinica:
    def __init__(self, paciente):
        self.__paciente__ = paciente
        self.__turnos__ = []
        self.__recetas__ = []

    def agregar_turno(self, turno):
        self.__turnos__.append(turno)

    def agregar_receta(self, receta):
        self.__recetas__.append(receta)

    def obtener_turnos(self):
        return list(self.__turnos__)

    def obtener_recetas(self):
        return list(self.__recetas__)

    def __str__(self):
        partes = [f"Historia clínica de: {self.__paciente__}"]
        partes.append("\nTurnos:")
        if self.__turnos__:
            for t in self.__turnos__:
                partes.append(f"- {t}")
        else:
            partes.append("(Sin turnos)")
        partes.append("\nRecetas:")
        if self.__recetas__:
            for r in self.__recetas__:
                partes.append(f"- {r}")
        else:
            partes.append("(Sin recetas)")
        return "\n".join(partes)
