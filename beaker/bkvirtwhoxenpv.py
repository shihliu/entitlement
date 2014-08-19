from beaker.beakerbase import BeakerBase
from utils.tools.shell.beakercmd import BeakerCMD
from utils.constants import VIRTWHO_XEN_FV_CONF, RHEL5_PACKAGES, KVM_JOB

class BKvirtwhoXENPV(BeakerBase):
    '''
    classdocs
    '''
    conf_file_name = VIRTWHO_XEN_FV_CONF

    def start(self, distro=None, sam_build=None, sam_server=None):
        if distro == None:
            distro = self.confs._confs["beakerdistro"]
        if sam_server == None:
            sam_server = self.confs._confs["samhostname"]
            sam_ip = self.confs._confs["samhostip"]
        else:
            sam_ip = sam_server

        beaker_command = BeakerCMD()

        if beaker_command.get_rhel_version(distro) == 5:
            RHEL5_PACKAGES.append("@xen")
            job_xml = beaker_command.create_runtime_job(KVM_JOB)
            beaker_command.set_beaker_distro_name(job_xml, distro)
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "HANDLEGUEST", self.confs._confs["handleguest"])
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "SAMHOSTNAME", sam_server)
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "SAMHOSTIP", sam_ip)
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "CONFILE", self.confs._confs["confile"])
            beaker_command.update_job_param(job_xml, "/distribution/entitlement-qa/Regression/virt-who", "COPYIMAGES", self.confs._confs["copyimages"])
            beaker_command.set_packages(job_xml, RHEL5_PACKAGES)
            beaker_command.set_beaker_job_name(job_xml, "Host/guest association test on %s(XEN/PV) against %s" % (distro, sam_build))
            beaker_command.set_beaker_distro_variant(job_xml, "")
            beaker_command.job_submit(job_xml)

if __name__ == "__main__":
    BKvirtwhoXENPV().start()
