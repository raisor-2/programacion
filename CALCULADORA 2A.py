import tkinter as tk
from tkinter import messagebox


class CalculadoraTkinter:

  def __init__(self, ventana):
    self.ventana = ventana
    self.ventana.title("Calculadora Tkinter - Historial")
    self.ventana.geometry("350x500")
    self.ventana.resizable(False, False)

    self.operacion = ""
    self.historial = []

    self.crear_widgets()

  def crear_widgets(self):
    # Pantalla
    self.pantalla_var = tk.StringVar()
    # CORREGIDO: Se cambia SUNETED por SUNKEN
    entry = tk.Entry(
        self.ventana,
        textvariable=self.pantalla_var,
        font=("Arial", 20),
        justify="right",
        bd=5,
        relief=tk.SUNKEN,
    )
    entry.pack(fill="x", padx=10, pady=10)

    # Frame de botones
    frame_botones = tk.Frame(self.ventana)
    frame_botones.pack(expand=True, fill="both", padx=10)

    botones = [
        ("7", 0, 0),
        ("8", 0, 1),
        ("9", 0, 2),
        ("/", 0, 3),
        ("4", 1, 0),
        ("5", 1, 1),
        ("6", 1, 2),
        ("*", 1, 3),
        ("1", 2, 0),
        ("2", 2, 1),
        ("3", 2, 2),
        ("-", 2, 3),
        ("0", 3, 0),
        ("C", 3, 1),
        ("=", 3, 2),
        ("+", 3, 3),
    ]

    for texto, fila, col in botones:
      btn = tk.Button(
          frame_botones,
          text=texto,
          font=("Arial", 14),
          fg="black",  # Números y símbolos en negro
          bg="#e2e8f0",
          command=lambda t=texto: self.accion(t),
      )
      btn.grid(row=fila, column=col, sticky="nsew", padx=2, pady=2)

    for i in range(4):
      frame_botones.rowconfigure(i, weight=1)
      frame_botones.columnconfigure(i, weight=1)

    # Historial
    tk.Label(
        self.ventana,
        text="Historial (últimas 5 operaciones):",
        font=("Arial", 10, "bold"),
    ).pack(anchor="w", padx=10)
    self.lbl_historial = tk.Label(
        self.ventana, text="", font=("Arial", 9), justify="left", bg="#f9f9f9"
    )
    self.lbl_historial.pack(fill="x", padx=10, pady=5)

  def accion(self, valor):
    if valor == "C":
      self.operacion = ""
      self.pantalla_var.set("")
    elif valor == "=":
      try:
        resultado = str(eval(self.operacion))
        item = f"{self.operacion} = {resultado}"

        self.historial.append(item)
        if len(self.historial) > 5:
          self.historial.pop(0)

        self.lbl_historial.config(text="\n".join(self.historial))
        self.pantalla_var.set(resultado)
        self.operacion = resultado
      except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir entre cero.")
        self.operacion = ""
        self.pantalla_var.set("")
      except Exception:
        messagebox.showerror("Error", "Operación inválida.")
        self.operacion = ""
        self.pantalla_var.set("")
    else:
      self.operacion += str(valor)
      self.pantalla_var.set(self.operacion)


if __name__ == "__main__":
  root = tk.Tk()
  app = CalculadoraTkinter(root)
  root.mainloop()