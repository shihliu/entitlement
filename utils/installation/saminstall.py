from utils.constants import SAM_INSTALLATION_CONF
from utils.installation.install import Install
from utils.tools.shell.virshcommand import VirshCommand

class SAMInstall(Install):
    '''
    classdocs
    '''
    conf_file_name = SAM_INSTALLATION_CONF

    def install_host(self):
        pass

    def install_guest(self, guest_name):
        remote_ip = self.confs._confs["installation_host_ip"]
        username = self.confs._confs["host_username"]
        password = self.confs._confs["host_password"]
        virsh_command = VirshCommand(remote_ip, username, password)
        virsh_command.create_vm(guest_name)

    def install_product(self):
        pass

if __name__ == "__main__":
    SAMInstall().start()
