class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        self.__tipo = tipo
        self.__dias = [d.lower() for d in dias]

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias

    def __str__(self):
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"
