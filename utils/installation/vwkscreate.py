from utils.constants import VIRTWHO_KICKSTART_CONF
from utils.installation.install import Install
from utils.tools.shell.virtwhokickstart import VirtWhoKickstart

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

if __name__ == "__main__":
    builds = VWKSCreate().check_build()
    VirtWhoKickstart().create(builds)
