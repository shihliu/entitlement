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

    def start(self, build=None):
        if build == None:
            new, build = self.check_build().strip("/")
            if new == -1:
                logger.info("No %s new build available yet, just exit ..." % self.product_name)
                return -1, build, ""
            else:
                logger.info("Found %s new build %s, begin installing ..." % (self.product_name, build))
                version = build.split("-")[1][:-2]
                beaker_command = BeakerCMD()
                job_xml = beaker_command.create_runtime_job("sam_latest_install_job_sample.xml")
                beaker_command.update_job_param(job_xml, "/installation/entitlement-qa/Install/sam-latest-install", "VERSION", version)
                job = beaker_command.job_submit(job_xml)
                sam_server = beaker_command.check_job_finished(job)
                return 0, build, sam_server
        else:
            logger.info("Install the latest %s build %s for virt-who testing, begin installing ..." % (self.product_name, build))
            version = build.split("-")[1][:-2]
            beaker_command = BeakerCMD()
            job_xml = beaker_command.create_runtime_job("sam_latest_install_job_sample.xml")
            beaker_command.update_job_param(job_xml, "/installation/entitlement-qa/Install/sam-latest-install", "VERSION", version)
            job = beaker_command.job_submit(job_xml)
            sam_server = beaker_command.check_job_finished(job)
            return 0, build, sam_server

if __name__ == "__main__":
    BKSAMInstall().start()
