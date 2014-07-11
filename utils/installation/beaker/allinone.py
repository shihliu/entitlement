from utils.installation.install import Install
from utils.installation.vwkscreate import VWKSCreate
from utils.installation.beaker.bkvirtwho import BKvirtwho
from utils.installation.beaker.bksaminstall import BKSAMInstall

class AllInOne(Install):
    '''
    classdocs
    '''
    conf_file_name = ""
    target_ip = ""

    def install_host(self):
        pass

    def install_guest(self, guest_name):
        pass

    def install_product(self, sam_compose):
        pass

    def start(self):
        new_rhel, build = VWKSCreate().start()
        new_sam, sam_server = BKSAMInstall().start()
        if new_rhel == 0 or new_sam == 0:
            BKvirtwho().start(build, sam_server)

if __name__ == "__main__":
    AllInOne().start()
