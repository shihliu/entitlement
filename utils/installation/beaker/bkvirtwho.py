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

    def start(self, distro=None, sam_build=None, sam_server=None):
            if distro == None:
                distro = self.confs._confs["beakerdistro"]
            if sam_server == None:
                sam_server = self.confs._confs["samhostname"]
                sam_ip = self.confs._confs["samhostip"]
            else:
                sam_ip = sam_server

            beaker_command = BeakerCMD()
            job_xml = beaker_command.create_runtime_job("virtwhobeaker_rhel_7_kvm_job_sample.xml")
            beaker_command.set_beaker_distro_name(job_xml, distro)

            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "HANDLEGUEST", self.confs._confs["handleguest"])
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "SAMHOSTNAME", sam_server)
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "SAMHOSTIP", sam_ip)
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "CONFILE", self.confs._confs["confile"])
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "COPYIMAGES", self.confs._confs["copyimages"])
            
            if beaker_command.get_rhel_version(distro) == 5:
                beaker_command.set_beaker_distro_variant(job_xml, "")

            beaker_command.set_beaker_job_name(job_xml, "Host/guest association test on %s(KVM) against %s" % (distro, sam_build))
            beaker_command.job_submit(job_xml)

if __name__ == "__main__":
    BKvirtwho().start()