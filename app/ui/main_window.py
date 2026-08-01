from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
)

from PySide6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("JARVIS OS")
        self.resize(1000, 700)

        self.setStyleSheet("""
            QMainWindow{
                background:#121212;
            }

            QLabel{
                color:white;
                font-size:18px;
            }

            QTextEdit{
                background:#1E1E1E;
                color:white;
                border:1px solid #333;
                border-radius:8px;
                font-size:15px;
            }

            QLineEdit{
                background:#1E1E1E;
                color:white;
                border:1px solid #333;
                border-radius:8px;
                padding:10px;
                font-size:15px;
            }

            QPushButton{
                background:#007ACC;
                color:white;
                border:none;
                border-radius:8px;
                padding:10px;
            }

            QPushButton:hover{
                background:#0099FF;
            }
        """)

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout()

        title = QLabel("🤖 JARVIS OS")
        title.setAlignment(Qt.AlignCenter)

        self.chat = QTextEdit()
        self.chat.setReadOnly(True)
        self.chat.setText(
            "Welcome to JARVIS OS\n\n"
            "Status: ONLINE\n\n"
            "Your AI assistant is ready."
        )

        self.input = QLineEdit()
        self.input.setPlaceholderText("Type your message...")

        send = QPushButton("Send")

        bottom = QHBoxLayout()
        bottom.addWidget(self.input)
        bottom.addWidget(send)

        layout.addWidget(title)
        layout.addWidget(self.chat)
        layout.addLayout(bottom)

        central.setLayout(layout)