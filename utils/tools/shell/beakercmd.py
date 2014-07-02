'''
commands to operate beaker
'''
import os
from utils import logger
from utils.tools.shell.command import Command

class BeakerCMD(Command):

    def job_submit(self, job_xml):
        "need beaker-client installed"
        cmd = "bkr job-submit job_xml"
        return self.run(cmd)

    def job_watch(self, job_id):
        "need beaker-client installed"
        cmd = "bkr job_watch job_xml"
        return self.run(cmd)

if __name__ == "__main__":
    beaker_command = BeakerCMD("10.66.128.31", "root", "redhat")
    beaker_command.import_manifest()
#     sam_command.add_sam_repo("SAM-1.4.0-RHEL-6-20140512.0")
