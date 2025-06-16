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
from datetime import datetime

class CLI:
    def __init__(self):
        self.clinica = Clinica()

    def ejecutar(self):
        while True:
            print("\n--- Menú Clínica ---")
            print("1) Agregar paciente")
            print("2) Agregar médico")
            print("3) Agendar turno")
            print("4) Agregar especialidad")
            print("5) Emitir receta")
            print("6) Ver historia clínica")
            print("7) Ver todos los turnos")
            print("8) Ver todos los pacientes")
            print("9) Ver todos los médicos")
            print("0) Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "0":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            elif opcion == "1":
                self.agregar_paciente()
            elif opcion == "2":
                self.agregar_medico()
            elif opcion == "3":
                self.agendar_turno()
            elif opcion == "4":
                self.agregar_especialidad_a_medico()
            elif opcion == "5":
                self.emitir_receta()
            elif opcion == "6":
                self.ver_historia_clinica()
            elif opcion == "7":
                self.ver_todos_los_turnos()
            elif opcion == "8":
                self.ver_todos_los_pacientes()
            elif opcion == "9":
                self.ver_todos_los_medicos()
            else:
                print("Funcionalidad no implementada aún.")

    def agregar_paciente(self):
        print("\n--- Agregar paciente ---")
        nombre = input("Nombre completo: ")
        dni = input("DNI: ")
        fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
        paciente = Paciente(nombre, dni, fecha_nacimiento)
        try:
            self.clinica.agregar_paciente(paciente)
            print("Paciente agregado correctamente.")
        except ValueError:
            print("Error: Ya existe un paciente con ese DNI.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def agregar_medico(self):
        print("\n--- Agregar médico ---")
        nombre = input("Nombre completo: ")
        matricula = input("Matrícula profesional: ")
        medico = Medico(nombre, matricula)
        try:
            self.clinica.agregar_medico(medico)
            print("Médico agregado correctamente.")
        except ValueError:
            print("Error: Ya existe un médico con esa matrícula.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def agendar_turno(self):
        print("\n--- Agendar turno ---")
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        especialidad = input("Especialidad: ")
        fecha_str = input("Fecha y hora (dd/mm/aaaa HH:MM): ")
        try:
            fecha_hora = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
        except ValueError:
            print("Error: Formato de fecha y hora incorrecto.")
            return
        try:
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("Turno agendado correctamente.")
        except PacienteNoEncontradoException:
            print("Error: Paciente no encontrado.")
        except MedicoNoDisponibleException as e:
            print(f"Error: {e}")
        except TurnoOcupadoException:
            print("Error: El médico ya tiene un turno en ese horario.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def agregar_especialidad_a_medico(self):
        print("\n--- Agregar especialidad a médico ---")
        matricula = input("Matrícula del médico: ")
        nombre_especialidad = input("Nombre de la especialidad: ")
        dias = input("Días de atención (separados por coma, ej: lunes,miércoles): ")
        dias_lista = [d.strip().lower() for d in dias.split(",") if d.strip()]
        try:
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            especialidad = Especialidad(nombre_especialidad, dias_lista)
            medico.agregar_especialidad(especialidad)
            print("Especialidad agregada correctamente al médico.")
        except Exception as e:
            print(f"Error: {e}")

    def emitir_receta(self):
        print("\n--- Emitir receta ---")
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        medicamentos = input("Medicamentos (separados por coma): ")
        lista_meds = [m.strip() for m in medicamentos.split(",") if m.strip()]
        try:
            receta = self.clinica.emitir_receta(dni, matricula, lista_meds)
            print("Receta emitida correctamente:")
            print(receta)
        except PacienteNoEncontradoException:
            print("Error: Paciente no encontrado.")
        except MedicoNoDisponibleException:
            print("Error: Médico no encontrado.")
        except RecetaInvalidaException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def ver_historia_clinica(self):
        print("\n--- Ver historia clínica ---")
        dni = input("DNI del paciente: ")
        try:
            historia = self.clinica.obtener_historia_clinica(dni)
            print(historia)
        except PacienteNoEncontradoException:
            print("Error: Paciente no encontrado.")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def ver_todos_los_turnos(self):
        print("\n--- Todos los turnos ---")
        turnos = self.clinica.obtener_turnos()
        if not turnos:
            print("No hay turnos registrados.")
        else:
            for turno in turnos:
                print(turno)

    def ver_todos_los_pacientes(self):
        print("\n--- Todos los pacientes ---")
        pacientes = self.clinica.obtener_pacientes()
        if not pacientes:
            print("No hay pacientes registrados.")
        else:
            for paciente in pacientes:
                print(paciente)

    def ver_todos_los_medicos(self):
        print("\n--- Todos los médicos ---")
        medicos = self.clinica.obtener_medicos()
        if not medicos:
            print("No hay médicos registrados.")
        else:
            for medico in medicos:
                print(medico) 