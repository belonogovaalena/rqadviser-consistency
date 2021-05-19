import os
import sys
from PyQt5.QtWidgets import QApplication


from rqadviser.model.m_main import ModelMain
from rqadviser.controller.ctrl_main import ControllerMain

if __name__ == '__main__':
    os.environ["QT_LOGGING_RULES"] = "*.debug=false"
    app = QApplication(sys.argv)
    model = ModelMain()
    controller = ControllerMain(model)
    sys.exit(app.exec_())

