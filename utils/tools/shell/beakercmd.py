'''
commands to operate beaker
need beaker-client installed
'''
from utils.tools.xmlparser.bkjobparser import BKJobParser
from utils.tools.shell.command import Command

class BeakerCMD(Command):

    def job_submit(self, job_xml):
        cmd = "bkr job-submit %s" % job_xml
        return self.run(cmd)

    def job_watch(self, job_id):
        cmd = "bkr job_watch %s" % job_id
        return self.run(cmd)

    def create_runtime_job(self, job_xml):
        return BKJobParser().runtime_job_copy(job_xml)

    def update_job_param(self, job_xml, task_name, parameter, value):
        BKJobParser(job_xml).update_param(task_name, parameter, value)

if __name__ == "__main__":
    pass
