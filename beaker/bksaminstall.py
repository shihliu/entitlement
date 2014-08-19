from utils import logger
from beaker.beakerbase import BeakerBase
from utils.tools.shell.beakercmd import BeakerCMD
from utils.constants import SAM_INSTALLATION_CONF, SAM_JOB

class BKSAMInstall(BeakerBase):
    '''
    classdocs
    '''
    conf_file_name = SAM_INSTALLATION_CONF

    def start(self, build=None):
        if build == None:
            new, build = self.check_build()
            if new == -1:
                logger.info("No %s new build available yet, just exit ..." % self.product_name)
                return -1, build, ""
            else:
                logger.info("Found %s new build %s, begin installing ..." % (self.product_name, build))
                return self.install_sam(build)
        else:
            logger.info("Install the latest %s build %s for virt-who testing, begin installing ..." % (self.product_name, build))
            return self.install_sam(build)

    def install_sam(self, build):
        version = build.split("-")[1][:-2]
        beaker_command = BeakerCMD()
        job_xml = beaker_command.create_runtime_job(SAM_JOB)
        beaker_command.update_job_param(job_xml, "/installation/entitlement-qa/Install/sam-latest-install", "VERSION", version)
        beaker_command.set_beaker_job_name(job_xml, "%s installation" % build)
        job = beaker_command.job_submit(job_xml)
        sam_server = beaker_command.check_job_finished(job)
        beaker_command.post_config_sam(sam_server)
        return 0, build, sam_server

if __name__ == "__main__":
    BKSAMInstall().start()
