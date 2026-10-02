import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class CalculadoraPySide6(QMainWindow):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("OrbitCalc Pro - Sistema de Cálculo")
    self.setFixedSize(420, 640)

    self.historial_lista = []
    self.operacion_actual = ""

    self.aplicar_estilos()
    self.inicializar_interfaz()
    self.inicializar_menu()

  def aplicar_estilos(self):
    # Se añade estilo explícito para la barra de menús y los menús desplegables con letras negras
    self.setStyleSheet("""
        QMainWindow {
            background-color: #f1f5f9;
        }
        QMenuBar {
            background-color: #e2e8f0;
            color: black;
            font-family: 'Segoe UI', Arial, sans-serif;
            font-weight: bold;
        }
        QMenuBar::item {
            background-color: transparent;
            color: black;
            padding: 6px 10px;
        }
        QMenuBar::item:selected {
            background-color: #cbd5e1;
            color: black;
        }
        QMenu {
            background-color: #ffffff;
            color: black;
            border: 1px solid #cbd5e1;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
        QMenu::item {
            color: black;
            padding: 6px 20px;
        }
        QMenu::item:selected {
            background-color: #e2e8f0;
            color: black;
        }
        QLabel {
            color: #1e293b;
            font-family: 'Segoe UI', Arial, sans-serif;
        }
        QLineEdit {
            background-color: #ffffff;
            color: black;
            border: 2px solid #cbd5e1;
            border-radius: 8px;
            font-size: 28px;
            font-weight: bold;
            font-family: 'Segoe UI', Arial, sans-serif;
            padding: 10px;
        }
        QPushButton {
            font-family: 'Segoe UI', Arial, sans-serif;
            border-radius: 8px;
            font-weight: bold;
        }
    """)

  def inicializar_interfaz(self):
    widget_central = QWidget()
    self.setCentralWidget(widget_central)
    layout_principal = QVBoxLayout(widget_central)
    layout_principal.setContentsMargins(20, 20, 20, 20)
    layout_principal.setSpacing(15)

    # Título Superior Elegante
    lbl_titulo = QLabel("◆ ORBITCALC PRO")
    lbl_titulo.setStyleSheet(
        "font-size: 14px; font-weight: bold; color: #0284c7; letter-spacing:"
        " 1px;"
    )
    layout_principal.addWidget(lbl_titulo)

    # Pantalla de resultados
    self.pantalla = QLineEdit()
    self.pantalla.setReadOnly(True)
    self.pantalla.setAlignment(Qt.AlignRight)
    layout_principal.addWidget(self.pantalla)

    # Cuadrícula de botones
    grid = QGridLayout()
    grid.setSpacing(8)

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
      btn.setMinimumHeight(50)

      # Estilos personalizados con texto en negro
      if texto in ["/", "*", "-", "+"]:
        btn.setStyleSheet(
            "background-color: #e0f2fe; color: black; border: 1px solid"
            " #bae6fd; font-size: 20px;"
        )
      elif texto == "=":
        btn.setStyleSheet(
            "background-color: #38bdf8; color: black; border: 1px solid"
            " #0284c7; font-size: 20px;"
        )
      elif texto == "C":
        btn.setStyleSheet(
            "background-color: #fee2e2; color: black; border: 1px solid"
            " #fecaca; font-size: 18px;"
        )
      else:
        btn.setStyleSheet(
            "background-color: #ffffff; color: black; border: 1px solid"
            " #cbd5e1; font-size: 18px;"
        )

      btn.clicked.connect(lambda checked, t=texto: self.boton_clic(t))
      grid.addWidget(btn, fila, col)

    layout_principal.addLayout(grid)

    # Sección Historial
    lbl_hist_titulo = QLabel("📋 Historial de Operaciones (Últimas 5):")
    lbl_hist_titulo.setStyleSheet(
        "font-size: 12px; font-weight: bold; color: #64748b;"
    )
    layout_principal.addWidget(lbl_hist_titulo)

    self.label_historial = QLabel("Sin operaciones recientes")
    self.label_historial.setStyleSheet(
        "font-size: 12px; color: black; background-color: #ffffff; border: 1px"
        " solid #cbd5e1; border-radius: 8px; padding: 10px;"
    )
    layout_principal.addWidget(self.label_historial)

  def inicializar_menu(self):
    barra_menu = self.menuBar()

    # Menú Archivo
    menu_archivo = barra_menu.addMenu("Archivo")
    accion_nueva = QAction("Nueva operación / Limpiar", self)
    accion_nueva.triggered.connect(self.limpiar_todo)
    menu_archivo.addAction(accion_nueva)
    menu_archivo.addSeparator()
    accion_salir = QAction("Salir", self)
    accion_salir.triggered.connect(self.close)
    menu_archivo.addAction(accion_salir)

    # Menú Editar
    menu_editar = barra_menu.addMenu("Editar")
    accion_copiar = QAction("Copiar resultado", self)
    accion_copiar.triggered.connect(
        lambda: QApplication.clipboard().setText(self.pantalla.text())
    )
    menu_editar.addAction(accion_copiar)
    accion_borrar = QAction("Borrar pantalla", self)
    accion_borrar.triggered.connect(self.limpiar_todo)
    menu_editar.addAction(accion_borrar)

    # Menú Ayuda
    menu_ayuda = barra_menu.addMenu("Ayuda")
    accion_acerca = QAction("Acerca de", self)
    accion_acerca.triggered.connect(self.mostrar_acerca_de)
    menu_ayuda.addAction(accion_acerca)
    accion_info = QAction("Información de la aplicación", self)
    accion_info.triggered.connect(self.mostrar_info)
    menu_ayuda.addAction(accion_info)

  def boton_clic(self, valor):
    if valor == "C":
      self.limpiar_todo()
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

  def limpiar_todo(self):
    self.operacion_actual = ""
    self.pantalla.clear()
    self.label_historial.setText("Sin operaciones recientes")

  def mostrar_acerca_de(self):
    QMessageBox.information(
        self,
        "Acerca de",
        "OrbitCalc Pro\nDesarrollado con PySide6 y diseño formal.",
    )

  def mostrar_info(self):
    QMessageBox.information(
        self,
        "Información",
        "Calculadora profesional equipada con sistema de menús, registro de"
        " historial dinámico y manejo de errores.",
    )


if __name__ == "__main__":
  app = QApplication(sys.argv)
  calc = CalculadoraPySide6()
  calc.show()
  sys.exit(app.exec())