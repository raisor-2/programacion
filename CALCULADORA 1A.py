import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class CalculadoraPySide6(QWidget):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Calculadora PySide6 - Historial")
    self.setFixedSize(400, 550)

    self.historial_lista = []
    self.operacion_actual = ""

    self.inicializar_interfaz()

  def inicializar_interfaz(self):
    layout_principal = QVBoxLayout(self)

    # Pantalla de resultados
    self.pantalla = QLineEdit()
    self.pantalla.setReadOnly(True)
    self.pantalla.setAlignment(Qt.AlignRight)
    self.pantalla.setStyleSheet(
        "font-size: 24px; padding: 10px; background-color: #f0f0f0;"
    )
    layout_principal.addWidget(self.pantalla)

    # Cuadrícula de botones
    grid = QGridLayout()
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
      btn = QPushButton(texto)
      btn.setStyleSheet("font-size: 18px; padding: 15px;")
      # CORREGIDO: Se usa un solo .connect
      btn.clicked.connect(lambda checked, t=texto: self.boton_clic(t))
      grid.addWidget(btn, fila, col)

    layout_principal.addLayout(grid)

    # Historial
    layout_principal.addWidget(QLabel("Historial (últimas 5 operaciones):"))
    self.label_historial = QLabel("")
    self.label_historial.setStyleSheet(
        "font-size: 12px; color: #555; background-color: #fff; padding: 5px;"
    )
    layout_principal.addWidget(self.label_historial)

  def boton_clic(self, valor):
    if valor == "C":
      self.operacion_actual = ""
      self.pantalla.clear()
    elif valor == "=":
      try:
        expr = (
            self.operacion_actual.replace("×", "*")
            .replace("÷", "/")
            .replace("x", "*")
        )
        resultado = str(eval(expr))
        texto_historial = f"{self.operacion_actual} = {resultado}"

        self.historial_lista.append(texto_historial)
        if len(self.historial_lista) > 5:
          self.historial_lista.pop(0)

        self.label_historial.setText("\n".join(self.historial_lista))
        self.pantalla.setText(resultado)
        self.operacion_actual = resultado
      except ZeroDivisionError:
        self.pantalla.setText("Error: Div / 0")
        self.operacion_actual = ""
      except Exception:
        self.pantalla.setText("Error")
        self.operacion_actual = ""
    else:
      self.operacion_actual += valor
      self.pantalla.setText(self.operacion_actual)


if __name__ == "__main__":
  app = QApplication(sys.argv)
  calc = CalculadoraPySide6()
  calc.show()
  sys.exit(app.exec())