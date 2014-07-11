from utils.constants import VIRTWHO_KICKSTART_CONF
from utils.installation.install import Install
from utils.tools.shell.virtwhokickstart import VirtWhoKickstart
from utils import logger

class VWKSCreate(Install):
    '''
    classdocs
    '''
    conf_file_name = VIRTWHO_KICKSTART_CONF
    target_ip = ""

    def install_host(self):
        pass

    def install_guest(self, guest_name):
        pass

    def install_product(self, sam_compose):
        pass

    def start(self):
        builds = self.check_build()
        if builds == "No New Build":
            logger.info("No rhel new build available yet, just exit ...")
            return -1, ""
        else:
            logger.info("Found rhel new build %s, begin creating virt-who kickstart file ..." % builds)
            VirtWhoKickstart().create(builds)
            return 0, builds

if __name__ == "__main__":
    VirtWhoKickstart().create("RHEL5.11-Server-20140709.0")
