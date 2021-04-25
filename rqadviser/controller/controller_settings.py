import os
from pathlib import Path
from datetime import datetime
from shutil import copyfile


class ControllerSettings:
    def __init__(self):
        pass

    def create_project(self, file_path, root):
        file_name = Path(file_path).name
        project_name = "{0}_{1}".format(file_name.split('.')[0], datetime.strftime(datetime.now(), "%Y%m%dT%H%M%S"))
        Path(os.path.join(root, project_name)).mkdir(parents=True, exist_ok=True)
        copyfile(file_path, os.path.join(root, project_name, file_name))
        return project_name
