from utils.constants import SAM_INSTALLATION_CONF
from utils.installation.install import Install
from utils.tools.shell.beakercmd import BeakerCMD
from utils import logger

class BKSAMInstall(Install):
    '''
    classdocs
    '''
    conf_file_name = SAM_INSTALLATION_CONF
    target_ip = ""

    def install_host(self):
        pass

    def install_guest(self, guest_name):
        pass

    def install_product(self, sam_compose):
        pass

    def start(self):
        new_build = self.check_build().strip("/")
        if new_build == "No New Build":
            logger.info("No %s new build available yet, just exit ..." % self.product_name)
            return -1, ""
        else:
            logger.info("Found %s new build %s, begin installing ..." % (self.product_name, new_build))
            version = new_build.split("-")[1][:-2]
            beaker_command = BeakerCMD()
            job_xml = beaker_command.create_runtime_job("sam_latest_install_job_sample.xml")
            beaker_command.update_job_param(job_xml, "/installation/entitlement-qa/Install/sam-latest-install", "VERSION", version)
            job = beaker_command.job_submit(job_xml)
            sam_server = beaker_command.check_job_finished(job)
            return 0, sam_server

if __name__ == "__main__":
    BKSAMInstall().start()
