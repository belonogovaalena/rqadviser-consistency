"""
Инициализация проекта
"""
import os
import sys
from configparser import ConfigParser
from logging import config
from pathlib import Path

from PyQt5.QtWidgets import QApplication

from rqadviser.controller.ctrl_main import ControllerMain
from rqadviser.model.m_main import ModelMain


def main():
    """
    Инициализация проекта
    """
    project_path = Path(__file__).parent.parent
    # сначала пытаемся определить путь в конфигурационном файла
    cfg_path = os.path.join(project_path, "cfg", "rqadviser-consistency.ini")
    cfg = ConfigParser()
    cfg.read(cfg_path)
    level = cfg.get("logger", "level")
    log_path = cfg.get("logger", "path")

    logging_config = {
        'version': 1,
        'loggers': {
            'rqadviser': {
                'level': level,
                'handlers': ['handler'],
            },
        },
        'handlers': {
            'handler': {
                'formatter': 'formatter',
                'class': 'logging.FileHandler',
                'filename': log_path,
                'mode': 'a',
            },
        },
        'formatters': {
            'formatter': {
                'format': '%(asctime)s-%(levelname)s-%(name)s::%(module)s|%(lineno)s:: %(message)s',
            },
        },
    }
    config.dictConfig(logging_config)
    os.environ["QT_LOGGING_RULES"] = "*.debug=false"
    app = QApplication(sys.argv)
    model = ModelMain()
    _ = ControllerMain(model)
    sys.exit(app.exec_())
