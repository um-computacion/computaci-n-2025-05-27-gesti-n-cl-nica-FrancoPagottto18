class Medico:
    def __init__(self, nombre: str, matricula: str):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = []

    def agregar_especialidad(self, especialidad):
        self.__especialidades.append(especialidad)

    def obtener_matricula(self):
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia):
        for esp in self.__especialidades:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None

    def __str__(self):
        if self.__especialidades:
            esp_str = ", ".join(str(e) for e in self.__especialidades)
        else:
            esp_str = "Sin especialidades"
        return f"{self.__nombre}, {self.__matricula}, [{esp_str}]"