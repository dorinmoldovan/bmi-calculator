import sys
from PyQt5.QtWidgets import QApplication
from gui.gui import BMICalculatorApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BMICalculatorApp()
    window.show()
    sys.exit(app.exec_())
