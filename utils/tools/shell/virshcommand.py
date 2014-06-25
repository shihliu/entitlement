'''
Use virsh API to manipulate vms
'''
import utils.constants, os
from utils import logger
from utils.tools.shell.command import Command

class VirshCommand(Command):

    def create_vm(self, guest_name):
        self.__create_storage()
        self.__create_img(guest_name)
        self.__unattended_install(guest_name)
        # Get guest IP
        guestip = self.__mac_to_ip(self.__get_dom_mac_addr(guest_name))

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
        virt-install -n SAM-1.4.0-RHEL-6-20140512.0 -r 2048 --vcpus=1 --os-variant=rhel6 --accelerate -v 
        --disk path=/home/auto-imgs/SAM-1.4.0-RHEL-6-20140512.0.img,size=20 
        -l http://download.englab.nay.redhat.com/pub/rhel/released/RHEL-6/6.5/Server/x86_64/os/ 
        --initrd-inject=/root/workspace/entitlement/data/kickstart/unattended/rhel-server-6-series.ks 
        --extra-args "ks=file:/rhel-server-6-series.ks"
        '''
        cmd = ('virt-install '
        '-n %s '
        '-r 2048 '
        '--vcpus=1 '
        '--os-variant=rhel6 '
        '--accelerate -v '
        '--disk path=/home/auto-imgs/%s.img,size=20 '
        '-l http://download.englab.nay.redhat.com/pub/rhel/released/RHEL-6/6.5/Server/x86_64/os/ '
        # '--nographics '
        '--initrd-inject=/root/workspace/entitlement/data/kickstart/unattended/rhel-server-6-series.ks '
        '--extra-args "ks=file:/rhel-server-6-series.ks"' % (guest_name, guest_name))
        self.run(cmd, timeout=3600)

    def __get_dom_mac_addr(self, domname):
        """
        Get mac address of a domain
        Return mac address on SUCCESS or None on FAILURE
        """
        cmd = "virsh dumpxml " + domname + " | grep 'mac address' | awk -F'=' '{print $2}' | tr -d \"[\'/>]\""
        (ret, out) = self.run(cmd)
        if ret == 0:
            return out
        else:
            return None

    def __mac_to_ip(self, mac, timeout=600):
        """
        Map mac address to ip
        Return None on FAILURE and the mac address on SUCCESS
        """
        if not mac:
            return None
        cmd = "sh " + os.path.realpath(os.path.join(os.path.dirname(__file__), "ipget.sh ")) + mac
        (ret, out) = self.run(cmd, timeout)
        return out

if __name__ == "__main__":
    pass

