
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QTextEdit,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFormLayout,
    QCheckBox,
    QRadioButton,
    QComboBox,
    QMessageBox,
    QDialog,
    QListWidget,
    QListWidgetItem,
    QGroupBox
)

from PySide6.QtCore import Qt


class DetalleDialog(QDialog):

    def __init__(self, datos, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Ficha del estudiante")
        self.resize(450, 350)

        layout = QVBoxLayout()

        titulo = QLabel("🎓 INFORMACIÓN DEL ESTUDIANTE")
        titulo.setStyleSheet(
            "font-size: 22px; font-weight: bold; color: black;"
        )

        informacion = QLabel(
            f"<b>Nombre:</b> {datos['nombre']}<br>"
            f"<b>CI:</b> {datos['ci']}<br>"
            f"<b>Curso:</b> {datos['curso']}<br>"
            f"<b>Turno:</b> {datos['turno']}<br>"
            f"<b>Actividades:</b> {datos['actividades'] or 'Ninguna'}<br>"
            f"<b>Observaciones:</b> "
            f"{datos['observaciones'] or 'Sin observaciones'}"
        )

        informacion.setWordWrap(True)
        informacion.setStyleSheet("color: black;")

        boton = QPushButton("Cerrar")
        boton.clicked.connect(self.accept)

        layout.addWidget(titulo)
        layout.addWidget(informacion)
        layout.addWidget(boton)

        self.setLayout(layout)

        self.setStyleSheet("""
            QDialog {
                background-color: white;
            }

            QPushButton {
                background-color: #487eb0;
                color: black;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }
        """)


class SistemaEstudiantes(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "Campus Nova - Registro de Estudiantes"
        )

        self.resize(1050, 680)

        self.registros = []
        self.indice_edicion = None

        self.crear_interfaz()

    def crear_interfaz(self):

        central = QWidget()
        self.setCentralWidget(central)

        principal = QVBoxLayout()
        central.setLayout(principal)

        # ============================================
        # ENCABEZADO
        # ============================================

        encabezado = QHBoxLayout()

        titulo = QLabel("🎓 CAMPUS NOVA")

        titulo.setStyleSheet("""
            color: black;
            font-size: 30px;
            font-weight: bold;
        """)

        subtitulo = QLabel(
            "Sistema de registro y seguimiento académico"
        )

        subtitulo.setStyleSheet("""
            color: black;
            font-size: 14px;
        """)

        encabezado.addWidget(titulo)
        encabezado.addStretch()
        encabezado.addWidget(subtitulo)

        principal.addLayout(encabezado)

        # ============================================
        # CONTENIDO
        # ============================================

        contenido = QHBoxLayout()

        # ============================================
        # PANEL IZQUIERDO
        # ============================================

        izquierda = QVBoxLayout()

        formulario = QFormLayout()

        self.nombre = QLineEdit()
        self.nombre.setPlaceholderText(
            "Ejemplo: María Pérez"
        )

        self.ci = QLineEdit()
        self.ci.setPlaceholderText(
            "Número de documento"
        )

        self.curso = QComboBox()

        self.curso.addItems([
            "1ro Secundaria",
            "2do Secundaria",
            "3ro Secundaria",
            "4to Secundaria",
            "5to Secundaria",
            "6to Secundaria"
        ])

        formulario.addRow(
            "Nombre completo:",
            self.nombre
        )

        formulario.addRow(
            "CI:",
            self.ci
        )

        formulario.addRow(
            "Curso:",
            self.curso
        )

        izquierda.addLayout(formulario)

        # ============================================
        # TURNO
        # ============================================

        grupo_turno = QGroupBox("Turno")

        turno_layout = QHBoxLayout()

        self.manana = QRadioButton("Mañana")
        self.tarde = QRadioButton("Tarde")

        self.manana.setChecked(True)

        turno_layout.addWidget(self.manana)
        turno_layout.addWidget(self.tarde)

        grupo_turno.setLayout(turno_layout)

        izquierda.addWidget(grupo_turno)

        # ============================================
        # ACTIVIDADES
        # ============================================

        grupo_actividades = QGroupBox(
            "Actividades favoritas"
        )

        actividades_layout = QGridLayout()

        self.deporte = QCheckBox("⚽ Deporte")
        self.musica = QCheckBox("🎵 Música")
        self.ciencia = QCheckBox("🔬 Ciencia")
        self.arte = QCheckBox("🎨 Arte")

        actividades_layout.addWidget(
            self.deporte, 0, 0
        )

        actividades_layout.addWidget(
            self.musica, 0, 1
        )

        actividades_layout.addWidget(
            self.ciencia, 1, 0
        )

        actividades_layout.addWidget(
            self.arte, 1, 1
        )

        grupo_actividades.setLayout(
            actividades_layout
        )

        izquierda.addWidget(
            grupo_actividades
        )

        # ============================================
        # OBSERVACIONES
        # ============================================

        etiqueta = QLabel("Observaciones:")

        etiqueta.setStyleSheet(
            "color: black; font-weight: bold;"
        )

        izquierda.addWidget(etiqueta)

        self.observaciones = QTextEdit()

        self.observaciones.setPlaceholderText(
            "Escribe observaciones del estudiante..."
        )

        izquierda.addWidget(
            self.observaciones
        )

        # ============================================
        # BOTONES
        # ============================================

        botones = QHBoxLayout()

        registrar = QPushButton("➕ Registrar")
        editar = QPushButton("✏️ Editar")
        eliminar = QPushButton("🗑 Eliminar")
        limpiar = QPushButton("🧹 Limpiar")

        botones.addWidget(registrar)
        botones.addWidget(editar)
        botones.addWidget(eliminar)
        botones.addWidget(limpiar)

        izquierda.addLayout(botones)

        # ============================================
        # PANEL DERECHO
        # ============================================

        derecha = QVBoxLayout()

        etiqueta_buscar = QLabel(
            "🔎 Buscar estudiante"
        )

        etiqueta_buscar.setStyleSheet(
            "color: black; font-weight: bold;"
        )

        derecha.addWidget(
            etiqueta_buscar
        )

        self.buscar = QLineEdit()

        self.buscar.setPlaceholderText(
            "Buscar por nombre o CI..."
        )

        derecha.addWidget(
            self.buscar
        )

        self.lista = QListWidget()

        derecha.addWidget(
            self.lista
        )

        ver = QPushButton(
            "👁️ Ver ficha completa"
        )

        derecha.addWidget(ver)

        contenido.addLayout(
            izquierda,
            3
        )

        contenido.addLayout(
            derecha,
            2
        )

        principal.addLayout(
            contenido
        )

        # ============================================
        # CONEXIONES
        # ============================================

        registrar.clicked.connect(
            self.registrar
        )

        editar.clicked.connect(
            self.editar
        )

        eliminar.clicked.connect(
            self.eliminar
        )

        limpiar.clicked.connect(
            self.limpiar
        )

        ver.clicked.connect(
            self.ver_ficha
        )

        self.buscar.textChanged.connect(
            self.actualizar_lista
        )

        # ============================================
        # ESTILOS
        # ============================================

        self.setStyleSheet("""
            QMainWindow {
                background-color: #f3f6fb;
                color: black;
            }

            QWidget {
                color: black;
            }

            QLabel {
                color: black;
            }

            QLineEdit,
            QTextEdit,
            QComboBox,
            QListWidget {
                background-color: white;
                color: black;
                border: 1px solid #ccd6e0;
                border-radius: 8px;
                padding: 7px;
            }

            QListWidget::item {
                color: black;
                padding: 10px;
            }

            QPushButton {
                background-color: #487eb0;
                color: black;
                border: none;
                border-radius: 8px;
                padding: 10px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #70a1ff;
                color: black;
            }

            QGroupBox {
                color: black;
                font-weight: bold;
                border: 1px solid #ccd6e0;
                border-radius: 10px;
                padding: 10px;
            }

            QRadioButton {
                color: black;
            }

            QCheckBox {
                color: black;
            }
        """)

    # ================================================
    # OBTENER DATOS
    # ================================================

    def obtener_datos(self):

        actividades = []

        if self.deporte.isChecked():
            actividades.append("Deporte")

        if self.musica.isChecked():
            actividades.append("Música")

        if self.ciencia.isChecked():
            actividades.append("Ciencia")

        if self.arte.isChecked():
            actividades.append("Arte")

        return {
            "nombre": self.nombre.text().strip(),
            "ci": self.ci.text().strip(),
            "curso": self.curso.currentText(),
            "turno": (
                "Mañana"
                if self.manana.isChecked()
                else "Tarde"
            ),
            "actividades": ", ".join(
                actividades
            ),
            "observaciones":
                self.observaciones
                .toPlainText()
                .strip()
        }

    # ================================================
    # VALIDACIÓN
    # ================================================

    def validar(self, datos):

        if len(datos["nombre"]) < 3:

            QMessageBox.warning(
                self,
                "Dato incorrecto",
                "El nombre debe tener al menos 3 caracteres."
            )

            return False

        if not datos["ci"].isdigit():

            QMessageBox.warning(
                self,
                "Dato incorrecto",
                "El CI debe contener solamente números."
            )

            return False

        return True

    # ================================================
    # REGISTRAR
    # ================================================

    def registrar(self):

        datos = self.obtener_datos()

        if not self.validar(datos):
            return

        if self.indice_edicion is not None:

            self.registros[
                self.indice_edicion
            ] = datos

            self.indice_edicion = None

            QMessageBox.information(
                self,
                "Actualizado",
                "El estudiante fue actualizado correctamente."
            )

        else:

            self.registros.append(
                datos
            )

            QMessageBox.information(
                self,
                "Registrado",
                "Estudiante registrado correctamente."
            )

        self.actualizar_lista()
        self.limpiar()

    # ================================================
    # ACTUALIZAR LISTA
    # ================================================

    def actualizar_lista(self):

        texto = self.buscar.text().lower()

        self.lista.clear()

        for i, estudiante in enumerate(
            self.registros
        ):

            if (
                texto in estudiante["nombre"].lower()
                or texto in estudiante["ci"].lower()
            ):

                item = QListWidgetItem(
                    f"🎓 {estudiante['nombre']} "
                    f"• {estudiante['curso']} "
                    f"• CI: {estudiante['ci']}"
                )

                item.setData(
                    Qt.UserRole,
                    i
                )

                self.lista.addItem(item)

    # ================================================
    # SELECCIONADO
    # ================================================

    def obtener_seleccionado(self):

        item = self.lista.currentItem()

        if item:
            return item.data(Qt.UserRole)

        return None

    # ================================================
    # EDITAR
    # ================================================

    def editar(self):

        indice = self.obtener_seleccionado()

        if indice is None:

            QMessageBox.information(
                self,
                "Aviso",
                "Selecciona un estudiante."
            )

            return

        estudiante = self.registros[indice]

        self.nombre.setText(
            estudiante["nombre"]
        )

        self.ci.setText(
            estudiante["ci"]
        )

        self.curso.setCurrentText(
            estudiante["curso"]
        )

        if estudiante["turno"] == "Mañana":
            self.manana.setChecked(True)
        else:
            self.tarde.setChecked(True)

        self.deporte.setChecked(
            "Deporte"
            in estudiante["actividades"]
        )

        self.musica.setChecked(
            "Música"
            in estudiante["actividades"]
        )

        self.ciencia.setChecked(
            "Ciencia"
            in estudiante["actividades"]
        )

        self.arte.setChecked(
            "Arte"
            in estudiante["actividades"]
        )

        self.observaciones.setPlainText(
            estudiante["observaciones"]
        )

        self.indice_edicion = indice

    # ================================================
    # ELIMINAR
    # ================================================

    def eliminar(self):

        indice = self.obtener_seleccionado()

        if indice is None:

            QMessageBox.information(
                self,
                "Aviso",
                "Selecciona un estudiante."
            )

            return

        respuesta = QMessageBox.question(
            self,
            "Confirmar eliminación",
            "¿Deseas eliminar este estudiante?"
        )

        if respuesta == QMessageBox.Yes:

            self.registros.pop(
                indice
            )

            self.actualizar_lista()
            self.limpiar()

    # ================================================
    # LIMPIAR
    # ================================================

    def limpiar(self):

        self.nombre.clear()
        self.ci.clear()
        self.observaciones.clear()

        self.curso.setCurrentIndex(0)

        self.manana.setChecked(True)

        self.deporte.setChecked(False)
        self.musica.setChecked(False)
        self.ciencia.setChecked(False)
        self.arte.setChecked(False)

        self.indice_edicion = None

    # ================================================
    # VER FICHA
    # ================================================

    def ver_ficha(self):

        indice = self.obtener_seleccionado()

        if indice is None:

            QMessageBox.information(
                self,
                "Aviso",
                "Selecciona un estudiante."
            )

            return

        dialogo = DetalleDialog(
            self.registros[indice],
            self
        )

        dialogo.exec()


# ================================================
# EJECUCIÓN
# ================================================

app = QApplication(sys.argv)

ventana = SistemaEstudiantes()

ventana.show()

sys.exit(app.exec())
