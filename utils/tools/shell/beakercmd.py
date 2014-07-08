'''
commands to operate beaker
need beaker-client installed
'''
import os
from utils.tools.xmlparser.xmlparser import XMLParser
from utils.tools.shell.command import Command

beakerjobs_path = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "data/beakerjobs/"))
runtime_path = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "runtime/"))

class BeakerCMD(Command):

    def job_submit(self, job_xml):
        cmd = "bkr job-submit %s" % job_xml
        return self.run(cmd)

    def job_watch(self, job_id):
        cmd = "bkr job_watch %s" % job_id
        return self.run(cmd)

    def create_sam_job_xml(self, build):
        version = build.split("-")[1][:-2]
        runtime_job = self.create_run_time_job("sam_latest_install_job_sample.xml")
        XMLParser("/root/workspace/entitlement/runtime/sam_latest_install_job_sample.xml").update_param("/installation/entitlement-qa/Install/sam-latest-install", "VERSION", version)
        return runtime_job

    def create_run_time_job(self, job_name):
        sample_job = beakerjobs_path + "/" + job_name
        XMLParser().xml_copy(sample_job, runtime_path)
        return runtime_path + "/" + job_name

if __name__ == "__main__":
    beaker_command = BeakerCMD()
    beaker_command.create_sam_job_xml("SAM-1.5.0-RHEL-6-20140512.0")
