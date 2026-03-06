import json
import os
import sys
import ctypes
from PyQt5 import QtCore, QtGui, QtWidgets
from pynput import keyboard

#Função para salvar as configurações do usuário.
CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {
        "outer_radius": 4,
        "inner_radius": 2,
        "size": 25,
        "color_index": 0,
        "first_run": True
    }

def save_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=4)

class MenuWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Crosshair Menu")
        self.setFixedSize(300, 200)

        self.config = load_config()

        layout = QtWidgets.QVBoxLayout()

        self.start_button = QtWidgets.QPushButton("Iniciar Crosshair")
        self.start_button.clicked.connect(self.start_crosshair)

        self.size_spin = QtWidgets.QSpinBox()
        self.size_spin.setRange(10, 200)
        self.size_spin.setValue(self.config["size"])
        self.size_spin.valueChanged.connect(self.update_size)

        self.style_combo = QtWidgets.QComboBox()
        self.style_combo.addItems(["circle", "cross", "dot", "x"])
        self.style_combo.setCurrentText(self.config.get("style", "circle"))
        self.style_combo.currentTextChanged.connect(self.update_style)

        layout.addWidget(QtWidgets.QLabel("Tamanho:"))
        layout.addWidget(self.size_spin)
        layout.addWidget(self.start_button)

        layout.addWidget(QtWidgets.QLabel("Estilo:"))
        layout.addWidget(self.style_combo)

        self.setLayout(layout)

        self.crosshair_window = None

    def update_size(self, value):
        self.config["size"] = value
        save_config(self.config)

    def update_style(self, value):
        self.config["style"] = value
        save_config(self.config)

    def start_crosshair(self):
        if not self.crosshair_window:
            self.crosshair_window = CrosshairWindow(
                outer_radius=self.config["outer_radius"],
                inner_radius=self.config["inner_radius"],
                size=self.config["size"]
            )
            self.crosshair_window.color_index = self.config["color_index"]
            self.crosshair_window.show()

            self.crosshair_window.style = self.config.get("style", "circle")

class CrosshairWindow(QtWidgets.QWidget):

    color_index_changed = QtCore.pyqtSignal(int)
    close_requested = QtCore.pyqtSignal()

    def __init__(self, outer_radius=5, inner_radius=3, size=25):
        super().__init__()
        # load stored config and apply provided parameters
        self.config = load_config()
        self.config["outer_radius"] = outer_radius
        self.config["inner_radius"] = inner_radius
        self.config["size"] = size
        self.style = self.config.get("style", "circle")
        flags = (
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.Tool
        )
        self.setWindowFlags(flags)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setFixedSize(size, size)

        self.outer_radius = outer_radius
        self.inner_radius = inner_radius

        self.colors = [
            QtGui.QColor("white"),
            QtGui.QColor("black"),
            QtGui.QColor("red"),
            QtGui.QColor("orangered"),
            QtGui.QColor("lime"),
            QtGui.QColor("green"),
            QtGui.QColor("darkgreen"),
            QtGui.QColor("cyan"),
            QtGui.QColor("blue"),
            QtGui.QColor("purple"),
            QtGui.QColor("magenta"),
        ]
        self.color_index = self.config.get("color_index", 0)

        self.color_index_changed.connect(self.on_color_index_changed)
        self.close_requested.connect(QtWidgets.QApplication.quit)

        self.center_on_screen()

        # IMPORTANTE: aplicar modo click-through no Windows
        self.make_click_through()

        self._listener = keyboard.Listener(on_press=self._on_key_press)
        self._listener.start()

    def make_click_through(self):
        hwnd = int(self.winId())

        GWL_EXSTYLE = -20
        WS_EX_LAYERED = 0x80000
        WS_EX_TRANSPARENT = 0x20

        user32 = ctypes.windll.user32
        current_style = user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        user32.SetWindowLongW(
            hwnd,
            GWL_EXSTYLE,
            current_style | WS_EX_LAYERED | WS_EX_TRANSPARENT
        )

    def center_on_screen(self):
        screen = QtWidgets.QApplication.primaryScreen()
        if not screen:
            return

        screen_center = screen.geometry().center()
        frame_geom = self.frameGeometry()
        frame_geom.moveCenter(screen_center)
        self.move(frame_geom.topLeft())

    def _on_key_press(self, key):
        try:
            if key == keyboard.Key.f1:
                next_index = (self.color_index + 1) % len(self.colors)
                self.color_index_changed.emit(next_index)

            elif key == keyboard.Key.f2:
                self.close_requested.emit()

        except Exception:
            pass

    @QtCore.pyqtSlot(int)
    def on_color_index_changed(self, index):
        self.color_index = index
        self.config["color_index"] = index
        save_config(self.config)
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        cx = self.width() // 2
        cy = self.height() // 2

        color = self.colors[self.color_index]
        pen = QtGui.QPen(color)
        pen.setWidth(2)
        painter.setPen(pen)
        painter.setBrush(QtCore.Qt.NoBrush)

        if self.style == "circle":
            painter.drawEllipse(
                QtCore.QRectF(
                    cx - self.outer_radius,
                    cy - self.outer_radius,
                    2 * self.outer_radius,
                    2 * self.outer_radius
                )
            )
            painter.drawEllipse(
                QtCore.QRectF(
                    cx - self.inner_radius,
                    cy - self.inner_radius,
                    2 * self.inner_radius,
                    2 * self.inner_radius
                )
            )

        elif self.style == "cross":
            size = self.outer_radius
            painter.drawLine(cx - size, cy, cx + size, cy)
            painter.drawLine(cx, cy - size, cx, cy + size)

        elif self.style == "dot":
            painter.setBrush(color)
            painter.drawEllipse(
                QtCore.QRectF(cx - 2, cy - 2, 4, 4)
            )

        elif self.style == "x":
            size = self.outer_radius
            painter.drawLine(cx - size, cy - size, cx + size, cy + size)
            painter.drawLine(cx - size, cy + size, cx + size, cy - size)

    def closeEvent(self, event):
        try:
            if self._listener and self._listener.running:
                self._listener.stop()
        except Exception:
            pass
        event.accept()

def main():
    app = QtWidgets.QApplication(sys.argv)
    config = load_config()

    if config.get("first_run", True):
        w = MenuWindow()
        w.show()
        config["first_run"] = False
        save_config(config)
        sys.exit(app.exec_())
    else:
        crosshair = CrosshairWindow(
            outer_radius=config["outer_radius"],
            inner_radius=config["inner_radius"],
            size=config["size"]
        )
        crosshair.color_index = config["color_index"]
        crosshair.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    main()