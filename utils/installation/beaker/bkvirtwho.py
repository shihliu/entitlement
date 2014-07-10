from utils.constants import VIRTWHO_RUN_CONF
from utils.installation.install import Install
from utils.tools.shell.beakercmd import BeakerCMD

class BKvirtwho(Install):
    '''
    classdocs
    '''
    conf_file_name = VIRTWHO_RUN_CONF
    target_ip = ""

    def install_host(self):
        pass

    def install_guest(self, guest_name):
        pass

    def install_product(self, sam_compose):
        pass

    def start(self):
#         new_build = self.check_build().strip("/")
#         if new_build == "No New Build":
#             logger.info("No %s new build available yet, just exit ..." % self.product_name)
#         else:
#             logger.info("Found %s new build %s, begin installing ..." % (self.product_name, new_build))
            beaker_command = BeakerCMD()
            job_xml = beaker_command.create_runtime_job("virtwhobeaker_rhel_7_kvm_job_sample.xml")
            beaker_command.set_beaker_distro(job_xml, self.confs._confs["beakerdistro"])

            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "HANDLEGUEST", self.confs._confs["handleguest"])
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "SAMHOSTNAME", self.confs._confs["samhostname"])
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "SAMHOSTIP", self.confs._confs["samhostip"])
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "CONFILE", self.confs._confs["confile"])
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "COPYIMAGES", self.confs._confs["copyimages"])

#             beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "VERSION", "1.4")
#             beaker_command.job_submit(job_xml)

if __name__ == "__main__":
    BKvirtwho().start()
