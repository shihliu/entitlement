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

    def create_sam_job_xml(self, build):
        version = build.split("-")[1][:-2]
        runtime_job = BKJobParser().runtime_job_copy("sam_latest_install_job_sample.xml")
        BKJobParser(runtime_job).update_param("/installation/entitlement-qa/Install/sam-latest-install", "VERSION", version)
        return runtime_job

if __name__ == "__main__":
    beaker_command = BeakerCMD()
    beaker_command.create_sam_job_xml("SAM-1.5.0-RHEL-6-20140512.0")
