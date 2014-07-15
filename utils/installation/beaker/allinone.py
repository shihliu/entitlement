from utils.installation.install import Install
from utils.installation.vwkscreate import VWKSCreate
from utils.installation.beaker.bkvirtwho import BKvirtwho
from utils.installation.beaker.bksaminstall import BKSAMInstall

class AllInOne():

    def start(self):
        new_rhel, build = VWKSCreate().start()
        new_sam, sam_build, sam_server = BKSAMInstall().start()
        if new_rhel == 0 or new_sam == 0:
            # if no sam new build, install the latest one
            if new_sam == -1:
                new_sam, sam_build, sam_server = BKSAMInstall().start(sam_build)
            BKvirtwho().start(build, sam_build, sam_server)

if __name__ == "__main__":
    AllInOne().start()
