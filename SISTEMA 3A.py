
import customtkinter as ctk
from tkinter import messagebox


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class SistemaEmpleados(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title(
            "Orbit HR - Registro de Empleados"
        )

        self.geometry(
            "1050x700"
        )

        self.configure(
            fg_color="#eef2f7"
        )

        self.empleados = []
        self.indice_edicion = None

        self.crear_interfaz()

    # =================================================
    # INTERFAZ
    # =================================================

    def crear_interfaz(self):

        titulo = ctk.CTkLabel(
            self,
            text="◈ ORBIT HR",
            font=("Arial", 30, "bold"),
            text_color="black"
        )

        titulo.pack(
            pady=(25, 5)
        )

        subtitulo = ctk.CTkLabel(
            self,
            text="Sistema de gestión de empleados",
            font=("Arial", 14),
            text_color="black"
        )

        subtitulo.pack(
            pady=(0, 20)
        )

        formulario = ctk.CTkFrame(
            self,
            fg_color="white"
        )

        formulario.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        # =================================================
        # NOMBRE
        # =================================================

        ctk.CTkLabel(
            formulario,
            text="Nombre completo:",
            text_color="black"
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.nombre = ctk.CTkEntry(
            formulario,
            width=280,
            fg_color="white",
            text_color="black"
        )

        self.nombre.grid(
            row=1,
            column=0,
            padx=15
        )

        # =================================================
        # CÓDIGO
        # =================================================

        ctk.CTkLabel(
            formulario,
            text="Código:",
            text_color="black"
        ).grid(
            row=0,
            column=1,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.codigo = ctk.CTkEntry(
            formulario,
            width=280,
            fg_color="white",
            text_color="black"
        )

        self.codigo.grid(
            row=1,
            column=1,
            padx=15
        )

        # =================================================
        # TELÉFONO
        # =================================================

        ctk.CTkLabel(
            formulario,
            text="Teléfono:",
            text_color="black"
        ).grid(
            row=2,
            column=0,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.telefono = ctk.CTkEntry(
            formulario,
            width=280,
            fg_color="white",
            text_color="black"
        )

        self.telefono.grid(
            row=3,
            column=0,
            padx=15
        )

        # =================================================
        # CORREO
        # =================================================

        ctk.CTkLabel(
            formulario,
            text="Correo:",
            text_color="black"
        ).grid(
            row=2,
            column=1,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.email = ctk.CTkEntry(
            formulario,
            width=280,
            fg_color="white",
            text_color="black"
        )

        self.email.grid(
            row=3,
            column=1,
            padx=15
        )

        # =================================================
        # DEPARTAMENTO
        # =================================================

        ctk.CTkLabel(
            formulario,
            text="Departamento:",
            text_color="black"
        ).grid(
            row=4,
            column=0,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.departamento = ctk.CTkComboBox(
            formulario,
            values=[
                "Tecnología",
                "Ventas",
                "Marketing",
                "Finanzas",
                "Recursos Humanos"
            ],
            width=280,
            text_color="black",
            fg_color="white",
            button_color="#3498db",
            dropdown_fg_color="white",
            dropdown_text_color="black"
        )

        self.departamento.grid(
            row=5,
            column=0,
            padx=15
        )

        self.departamento.set(
            "Tecnología"
        )

        # =================================================
        # CARGO
        # =================================================

        ctk.CTkLabel(
            formulario,
            text="Cargo:",
            text_color="black"
        ).grid(
            row=4,
            column=1,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.cargo = ctk.CTkComboBox(
            formulario,
            values=[
                "Analista",
                "Asistente",
                "Supervisor",
                "Coordinador",
                "Gerente"
            ],
            width=280,
            text_color="black",
            fg_color="white",
            button_color="#3498db",
            dropdown_fg_color="white",
            dropdown_text_color="black"
        )

        self.cargo.grid(
            row=5,
            column=1,
            padx=15
        )

        self.cargo.set(
            "Analista"
        )

        # =================================================
        # CONTRATO
        # =================================================

        ctk.CTkLabel(
            formulario,
            text="Tipo de contrato:",
            text_color="black"
        ).grid(
            row=6,
            column=0,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.contrato = ctk.CTkComboBox(
            formulario,
            values=[
                "Indefinido",
                "Plazo fijo",
                "Medio tiempo",
                "Prácticas"
            ],
            width=280,
            text_color="black",
            fg_color="white",
            button_color="#3498db",
            dropdown_fg_color="white",
            dropdown_text_color="black"
        )

        self.contrato.grid(
            row=7,
            column=0,
            padx=15
        )

        self.contrato.set(
            "Indefinido"
        )

        # =================================================
        # ACTIVO
        # =================================================

        self.activo = ctk.BooleanVar(
            value=True
        )

        ctk.CTkCheckBox(
            formulario,
            text="Empleado activo",
            variable=self.activo,
            text_color="black",
            fg_color="#3498db",
            hover_color="#2980b9"
        ).grid(
            row=7,
            column=1,
            padx=15,
            sticky="w"
        )

        # =================================================
        # HABILIDADES
        # =================================================

        ctk.CTkLabel(
            formulario,
            text="Habilidades:",
            text_color="black"
        ).grid(
            row=8,
            column=0,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.habilidades = ctk.CTkEntry(
            formulario,
            width=580,
            placeholder_text="Python, Excel, liderazgo...",
            text_color="black",
            fg_color="white"
        )

        self.habilidades.grid(
            row=9,
            column=0,
            columnspan=2,
            padx=15,
            sticky="ew"
        )

        # =================================================
        # OBSERVACIONES
        # =================================================

        ctk.CTkLabel(
            formulario,
            text="Observaciones:",
            text_color="black"
        ).grid(
            row=10,
            column=0,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.observaciones = ctk.CTkTextbox(
            formulario,
            width=580,
            height=100,
            text_color="black",
            fg_color="white"
        )

        self.observaciones.grid(
            row=11,
            column=0,
            columnspan=2,
            padx=15,
            sticky="ew"
        )

        # =================================================
        # BOTONES
        # =================================================

        botones = ctk.CTkFrame(
            formulario,
            fg_color="transparent"
        )

        botones.grid(
            row=12,
            column=0,
            columnspan=2,
            pady=20
        )

        ctk.CTkButton(
            botones,
            text="💾 Registrar",
            command=self.registrar,
            text_color="black"
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            botones,
            text="✏️ Editar",
            command=self.editar,
            text_color="black"
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            botones,
            text="🔎 Buscar",
            command=self.buscar,
            text_color="black"
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            botones,
            text="🗑️ Eliminar",
            command=self.eliminar,
            fg_color="#e74c3c",
            hover_color="#c0392b",
            text_color="black"
        ).pack(
            side="left",
            padx=5
        )

        ctk.CTkButton(
            botones,
            text="🧹 Limpiar",
            command=self.limpiar,
            fg_color="#bdc3c7",
            hover_color="#95a5a6",
            text_color="black"
        ).pack(
            side="left",
            padx=5
        )

    # =================================================
    # OBTENER DATOS
    # =================================================

    def obtener_datos(self):

        return {
            "nombre":
                self.nombre.get().strip(),

            "codigo":
                self.codigo.get().strip(),

            "telefono":
                self.telefono.get().strip(),

            "email":
                self.email.get().strip(),

            "departamento":
                self.departamento.get(),

            "cargo":
                self.cargo.get(),

            "contrato":
                self.contrato.get(),

            "activo":
                self.activo.get(),

            "habilidades":
                self.habilidades.get().strip(),

            "observaciones":
                self.observaciones
                .get("1.0", "end")
                .strip()
        }

    # =================================================
    # VALIDAR
    # =================================================

    def validar(self, datos):

        if len(datos["nombre"]) < 3:

            messagebox.showwarning(
                "Validación",
                "Escribe un nombre válido."
            )

            return False

        if datos["codigo"] == "":

            messagebox.showwarning(
                "Validación",
                "Escribe el código del empleado."
            )

            return False

        if "@" not in datos["email"]:

            messagebox.showwarning(
                "Validación",
                "Escribe un correo electrónico válido."
            )

            return False

        return True

    # =================================================
    # REGISTRAR
    # =================================================

    def registrar(self):

        datos = self.obtener_datos()

        if not self.validar(datos):
            return

        if self.indice_edicion is not None:

            self.empleados[
                self.indice_edicion
            ] = datos

            messagebox.showinfo(
                "Actualizado",
                "Empleado actualizado correctamente."
            )

            self.indice_edicion = None

        else:

            self.empleados.append(
                datos
            )

            messagebox.showinfo(
                "Registrado",
                "Empleado registrado correctamente."
            )

        self.limpiar()

    # =================================================
    # BUSCAR
    # =================================================

    def buscar(self):

        if len(self.empleados) == 0:

            messagebox.showinfo(
                "Empleados",
                "No existen empleados registrados."
            )

            return

        texto = ""

        for empleado in self.empleados:

            texto += (
                f"Nombre: "
                f"{empleado['nombre']}\n"

                f"Código: "
                f"{empleado['codigo']}\n"

                f"Departamento: "
                f"{empleado['departamento']}\n"

                f"Cargo: "
                f"{empleado['cargo']}\n"

                f"Contrato: "
                f"{empleado['contrato']}\n"

                f"Activo: "
                f"{'Sí' if empleado['activo'] else 'No'}\n"

                f"Habilidades: "
                f"{empleado['habilidades']}\n"

                f"Observaciones: "
                f"{empleado['observaciones']}\n"

                f"--------------------------------\n"
            )

        messagebox.showinfo(
            "Lista de empleados",
            texto
        )

    # =================================================
    # EDITAR
    # =================================================

    def editar(self):

        if len(self.empleados) == 0:

            messagebox.showinfo(
                "Aviso",
                "Primero registra un empleado."
            )

            return

        self.indice_edicion = 0

        empleado = self.empleados[0]

        self.nombre.delete(
            0,
            "end"
        )

        self.nombre.insert(
            0,
            empleado["nombre"]
        )

        self.codigo.delete(
            0,
            "end"
        )

        self.codigo.insert(
            0,
            empleado["codigo"]
        )

        self.telefono.delete(
            0,
            "end"
        )

        self.telefono.insert(
            0,
            empleado["telefono"]
        )

        self.email.delete(
            0,
            "end"
        )

        self.email.insert(
            0,
            empleado["email"]
        )

        self.departamento.set(
            empleado["departamento"]
        )

        self.cargo.set(
            empleado["cargo"]
        )

        self.contrato.set(
            empleado["contrato"]
        )

        self.activo.set(
            empleado["activo"]
        )

        self.habilidades.delete(
            0,
            "end"
        )

        self.habilidades.insert(
            0,
            empleado["habilidades"]
        )

        self.observaciones.delete(
            "1.0",
            "end"
        )

        self.observaciones.insert(
            "1.0",
            empleado["observaciones"]
        )

        messagebox.showinfo(
            "Editar",
            "Modifica los datos y pulsa Registrar."
        )

    # =================================================
    # ELIMINAR
    # =================================================

    def eliminar(self):

        if len(self.empleados) == 0:

            messagebox.showinfo(
                "Aviso",
                "No existen empleados registrados."
            )

            return

        respuesta = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Deseas eliminar el primer empleado registrado?"
        )

        if respuesta:

            self.empleados.pop(0)

            messagebox.showinfo(
                "Eliminado",
                "Empleado eliminado correctamente."
            )

    # =================================================
    # LIMPIAR
    # =================================================

    def limpiar(self):

        self.nombre.delete(
            0,
            "end"
        )

        self.codigo.delete(
            0,
            "end"
        )

        self.telefono.delete(
            0,
            "end"
        )

        self.email.delete(
            0,
            "end"
        )

        self.habilidades.delete(
            0,
            "end"
        )

        self.departamento.set(
            "Tecnología"
        )

        self.cargo.set(
            "Analista"
        )

        self.contrato.set(
            "Indefinido"
        )

        self.activo.set(True)

        self.observaciones.delete(
            "1.0",
            "end"
        )

        self.indice_edicion = None


# =====================================================
# EJECUTAR
# =====================================================

if __name__ == "__main__":

    app = SistemaEmpleados()

    app.mainloop()

