'''
Use virsh API to manipulate vms
'''
import utils.constants, os, time
from utils import logger
from utils.tools.shell.command import Command

class VirshCommand(Command):

    def create_vm(self, guest_name):
#         self.__create_storage()
#         self.__create_img(guest_name)
        self.__unattended_install(guest_name)
        return self.__check_vm_available(guest_name)

    def __check_vm_available(self, guest_name, timeout=600):
        terminate_time = time.time() + timeout
        while True:
            guestip = self.__mac_to_ip(self.__get_dom_mac_addr(guest_name))
            if guestip != "":
                return guestip
            if terminate_time < time.time():
                raise OSError("Process timeout has been reached")
            logger.debug("Check guest IP, wait 1 minute ...")
            time.sleep(60)

    def find_vm(self, guest_name):
        # Get guest IP
        guestip = self.__mac_to_ip(self.__get_dom_mac_addr(guest_name))
        return guestip

    def define_vm(self):
        pass
    
    def clone_vm(self):
        pass

    def __create_img(self, img_name, path="/home/auto-imgs/", size=20):
        cmd = "qemu-img create -f raw %s%s.img %sG" % (path, img_name, size)
        self.run(cmd, timeout=None)

    def __create_storage(self, path="/home/auto-imgs/"):
        cmd = "mkdir -p %s" % path
        self.run(cmd, timeout=None)

    def __unattended_install(self, guest_name):
        '''
        install a guest with virt-install command, need virt-install tool installed:
        can not quite normally, check ip to make sure guest installed temperatelly
        '''
        cmd = ('virt-install '
#                '--network=bridge:br0 '
               '--initrd-inject=/root/workspace/entitlement/data/kickstart/unattended/rhel-server-6-series.ks '
               '--extra-args "ks=file:/rhel-server-6-series.ks" '
               '--name=%s '
               '--disk path=/home/auto-imgs/%s.img,size=20 '
               '--ram 2048 '
               '--vcpus=1 '
               '--check-cpu '
               '--accelerate '
               '--hvm '
               '--location=http://download.englab.nay.redhat.com/pub/rhel/released/RHEL-6/6.5/Server/x86_64/os/ '
#                 '--nographics '
               % (guest_name, guest_name))
        self.run(cmd, timeout=600)

    def __get_dom_mac_addr(self, domname):
        """
        Get mac address of a domain
        Return mac address on SUCCESS or None on FAILURE
        """
        cmd = "virsh dumpxml " + domname + " | grep 'mac address' | awk -F'=' '{print $2}' | tr -d \"[\'/>]\""
        (ret, out) = self.run(cmd)
        if ret == 0:
            return out.strip("\n").strip(" ")
        else:
            return None

    def __mac_to_ip(self, mac):
        """
        Map mac address to ip
        Return None on FAILURE and the mac address on SUCCESS
        """
        if not mac:
            return None
        cmd = "sh " + os.path.realpath(os.path.join(os.path.dirname(__file__), "ipget.sh ")) + mac
        (ret, out) = self.run(cmd)
        return out.strip("\n").strip(" ")

if __name__ == "__main__":
    virsh_command = VirshCommand()
    print virsh_command.create_vm("AUTO-SAM-1.4.0-RHEL-6-20140512.0")
    pass
# "virt-clone --connect=qemu:///system -o srchost -n newhost -f /path/to/newhost.qcow2"

