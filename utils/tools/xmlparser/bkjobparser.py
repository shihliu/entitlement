import os
from utils import constants
from utils.tools.xmlparser.xmlparser import XMLParser

class BKJobParser(XMLParser):

    beakerjobs_path = constants.BEAKER_JOBS_PATH
    runtime_path = constants.RUNTIME_PATH

    def update_param(self, task_name, param_name, param_value):
        for taskitem in self.root.getElementsByTagName("task"):
            if taskitem.getAttribute("name") == task_name:
                for paramitem in taskitem.getElementsByTagName("param"):
                    if paramitem.getAttribute("name") == param_name:
                        paramitem.setAttribute("value", param_value)
                        self.write_xml()

    def update_distroRequires(self, distro_name):
        for item in self.root.getElementsByTagName("distroRequires"):
            item.getElementsByTagName("distro_name").setAttribute("value", distro_name)
            self.write_xml()

    @classmethod
    def runtime_job_copy(self, job_xml):
        if not self.check_path_exist(self.runtime_path):
            self.create_path(self.runtime_path)
        self.xml_copy(os.path.join(self.beakerjobs_path, job_xml), self.runtime_path)
        return os.path.join(self.runtime_path, job_xml)

if __name__ == "__main__":
    pass
