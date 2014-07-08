from utils.constants import SAM_INSTALLATION_CONF
from utils.installation.install import Install
from utils.tools.shell.beakercmd import BeakerCMD
from utils import logger
from utils.tools.xmlparser import buildxml

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
        else:
            logger.info("Found %s new build %s, begin installing ..." % (self.product_name, new_build))

        beaker_command = BeakerCMD()
        job_xml = beaker_command.create_sam_job_xml(new_build)
        beaker_command.job_submit(job_xml)

if __name__ == "__main__":
    BKSAMInstall().start()
