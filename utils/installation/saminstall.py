from utils.constants import SAM_INSTALLATION_CONF
from utils.installation.install import Install

class SAMInstall(Install):
    '''
    classdocs
    '''
    conf_file_name = SAM_INSTALLATION_CONF
    product_name = "SAM"

    def install_host(self):
        pass

    def install_guest(self):
        pass

    def install_product(self):
        pass

if __name__ == "__main__":
    SAMInstall().start()
