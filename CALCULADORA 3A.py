import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class CalculadoraToga(toga.App):

  def startup(self):
    self.main_window = toga.MainWindow(title="Calculadora Toga", size=(350, 500))
    self.operacion = ""
    self.historial = []

    # Pantalla
    self.pantalla = toga.TextInput(readonly=True, style=Pack(flex=1, padding=5))

    # Historial visual (multilínea)
    self.lbl_historial = toga.MultilineTextInput(
        readonly=True, style=Pack(flex=2, padding=5)
    )

    # Contenedor general
    main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
    main_box.add(self.pantalla)

    # Botones distribuidos en filas
    filas = [["7", "8", "9", "/"], ["4", "5", "6", "*"], ["1", "2", "3", "-"], ["0", "C", "=", "+"]]

    for fila in filas:
      fila_box = toga.Box(style=Pack(direction=ROW, padding=2))
      for texto in fila:
        btn = toga.Button(
            texto,
            on_press=self.al_presionar_boton,
            style=Pack(flex=1, padding=2),
        )
        fila_box.add(btn)
      main_box.add(fila_box)

    main_box.add(toga.Label("Historial (últimas 5):", style=Pack(padding_top=5)))
    main_box.add(self.lbl_historial)

    self.main_window.content = main_box
    self.main_window.show()

  def al_presionar_boton(self, widget):
    texto = widget.text
    if texto == "C":
      self.operacion = ""
      self.pantalla.value = ""
    elif texto == "=":
      try:
        resultado = str(eval(self.operacion))
        item = f"{self.operacion} = {resultado}"

        self.historial.append(item)
        if len(self.historial) > 5:
          self.historial.pop(0)

        self.lbl_historial.value = "\n".join(self.historial)
        self.pantalla.value = resultado
        self.operacion = resultado
      except ZeroDivisionError:
        self.pantalla.value = "Error: Div/0"
        self.operacion = ""
      except Exception:
        self.pantalla.value = "Error"
        self.operacion = ""
    else:
      self.operacion += texto
      self.pantalla.value = self.operacion


def main():
  return CalculadoraToga("Calculadora Toga", "org.beeware.calculadora")


if __name__ == "__main__":
  main().main_loop()