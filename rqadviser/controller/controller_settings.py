import os
import platform
import getpass
from pathlib import Path
from datetime import datetime
from shutil import copyfile
from configparser import ConfigParser


class ControllerSettings:
    def __init__(self):
        pass

    @staticmethod
    def create_project(file_path, root):
        file_name = Path(file_path).name
        project_name = "{0}_{1}".format(file_name.split('.')[0], datetime.strftime(datetime.now(), "%Y%m%dT%H%M%S"))
        Path(os.path.join(root, project_name)).mkdir(parents=True, exist_ok=True)
        copyfile(file_path, os.path.join(root, project_name, 'data.csv'))
        return project_name

    @staticmethod
    def init_saves_path():
        saves_path = ""
        project_path = Path(__file__).parent.parent.parent
        cfg_path = os.path.join(project_path, "cfg", "rqadviser-consistency.ini")
        if os.path.exists(cfg_path):
            config = ConfigParser()
            config.read(cfg_path)
            saves_path = config.get("settings", "root")
        else:
            if platform.system() == "Linux":
                return "/home/{0}/output/rqadviser".format(getpass.getuser())
            elif platform.system() == "Windows":
                return "C:\\Users\\{0}\\rqadviser".format(getpass.getuser())
        return saves_path
