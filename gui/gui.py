from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QColor
from calculator.calculator import calculate_bmi, interpret_bmi

class BMICalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setFixedSize(300, 150)

        layout = QVBoxLayout()

        self.height_label = QLabel("Height (m):")
        self.height_input = QLineEdit()
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)

        self.weight_label = QLabel("Weight (kg):")
        self.weight_input = QLineEdit()
        layout.addWidget(self.weight_label)
        layout.addWidget(self.weight_input)

        self.calculate_button = QPushButton("Calculate BMI")
        self.calculate_button.clicked.connect(self.calculate_bmi)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate_bmi(self):
        try:
            height = float(self.height_input.text())
            weight = float(self.weight_input.text())
            bmi = calculate_bmi(height, weight)
            interpretation, color = interpret_bmi(bmi)
            self.result_label.setText(f"Your BMI is: {bmi:.2f} - {interpretation}")
            self.result_label.setStyleSheet(f"color: {color};")
        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please enter valid numbers for height and weight.")
