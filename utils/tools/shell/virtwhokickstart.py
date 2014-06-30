'''
commands to create virt-who kickstart file
make sure repo/distros exist, add repo/profiles/ and repo/kickstarts/libvirt/RHEL[5,6,7]/ 
'''
import os
from utils import logger
from utils.tools.shell.command import Command

manifest_name = "sam_install_manifest.zip"
sam_manifest = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "data/manifest/%s" % manifest_name))

class VirtWhoKickstart(Command):

    def create(self, compose):
        # RHEL6.4-20130130.0
        build = compose.split("-")[0].replace(".", "u")
        date = compose.split("-")[1]
        distro_name = "%s-Server-x64-%s.distro" % (build, date)
        profile_name = "ent-%s-server-x64-%s-kvm-libvirt.profile" % (build, date)
        kickstart_name = "ent-ks-%s-server-x64-%s-kvm-libvirt.cfg" % (build, date)
        self.__check_git_repo()
        self.__check_distro(distro_name)
        self.__create_kickstart(kickstart_name)
        self.__create_profile(profile_name, distro_name, kickstart_name)
        self.__git_push(profile_name, kickstart_name)

    def __check_git_repo(self):
        check_folder_exist
        if True:
            logger.info("git repo not exist, cloning now ...")
            cmd = "git clone git+ssh://git@qe-git.englab.nay.redhat.com/~/repo/virt-qe/repo"
            self.run(cmd)
        cmd = "git pull"
        self.run(cmd)

    def __check_distro(self, distro_name):
        check_file_exist
        if True:
            logger.info("git repo not exist, cloning now ...")
            cmd = "git clone git+ssh://git@qe-git.englab.nay.redhat.com/~/repo/virt-qe/repo"
            self.run(cmd)
        cmd = "git pull"
        self.run(cmd)

    def __get_rhel_version(self, distro_name):
        if distro_name.startwith("RHEL5"):
            return 5
        elif distro_name.startwith("RHEL7"):
            return 6
        elif distro_name.startwith("RHEL7"):
            return 7


    def __create_profile(self, profile_name, distro_name, kickstart_name):
        check_file_exist
        cmd = ('cat <<EOF > repo/profiles/%s\n'
            '[General]\n'
            'distro = %s\n'
            'kickstart = libvirt/RHEL%s/%s\n'
            'EOF' % (profile_name, distro_name, self.__get_rhel_version(distro_name), kickstart_name)
            )
        
        self.run(cmd)

    def __create_kickstart(self, kickstart_name):
        check_file_exist
        if True:
            logger.info("git repo not exist, cloning now ...")
            cmd = "git clone git+ssh://git@qe-git.englab.nay.redhat.com/~/repo/virt-qe/repo"
            self.run(cmd)
        cmd = "git pull"
        self.run(cmd)

    def __git_push(self, profile_name, kickstart_name):
            cmd = "git add %s %s " % (profile_name, kickstart_name)
            self.run(cmd)
            cmd = "git commit - m 'Auto add virt-who kickstart file: %s %s' " % (profile_name, kickstart_name)
            self.run(cmd)
            cmd = "git push" % (profile_name, kickstart_name)
            self.run(cmd)

    def check_file_exist(self, file_name):
        return os.path.isfile(file_name)

    def check_path_exist(self, path_name):
        return os.path.exists(path_name)

if __name__ == "__main__":
    virt_who_kick = VirtWhoKickstart().create("")
#     sam_command.add_sam_repo("SAM-1.4.0-RHEL-6-20140512.0")

