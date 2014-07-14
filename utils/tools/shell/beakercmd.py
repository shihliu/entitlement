'''
commands to operate beaker
need beaker-client installed
'''
import time
from utils.tools.xmlparser.bkjobparser import BKJobParser
from utils.tools.shell.command import Command

class BeakerCMD(Command):

    def job_submit(self, job_xml):
        cmd = "bkr job-submit %s" % job_xml
        retcode, output = self.run(cmd)
        if retcode == 0:
            # Submitted: ['J:693133']
            job_id = output.strip("\n").split("[")[1].strip("'").strip("]").strip("'")
        return job_id

    def job_watch(self, job_id):
        cmd = "bkr job_watch %s" % job_id
        return self.run(cmd)

    def create_runtime_job(self, job_xml):
        return BKJobParser().runtime_job_copy(job_xml)

    def update_job_param(self, job_xml, task_name, parameter, value):
        BKJobParser(job_xml).update_param(task_name, parameter, value)

    def set_beaker_distro(self, job_xml, distro_name):
        BKJobParser(job_xml).update_distroRequires(distro_name)

    def check_job_finished(self, job_id):
        cmd = "bkr job-logs %s | grep 'test_log--distribution-reservesys.log'" % job_id
        while True:
            retcode, output = self.run(cmd)
            if retcode == 0:
                reserved_machine = output.split("/")[2]
                return reserved_machine
            time.sleep(60)

if __name__ == "__main__":
    pass
