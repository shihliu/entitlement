'''
commands to create virt-who kickstart file
make sure repo/distros exist, add repo/profiles/ and repo/kickstarts/libvirt/RHEL[5,6,7]/ 
'''
import os, time
from utils import logger
from utils.tools.shell.command import Command

manifest_name = "sam_install_manifest.zip"
kickstart_repo_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), "repo"))
dir_sample_kickstart = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "data/kickstart/"))

class VirtWhoKickstart(Command):

    def create(self, compose):
        # RHEL6.4-20130130.0
        build = compose.split("-")[0].replace(".", "u")
        date = compose.split("-")[1]
        distro_name = "%s-Server-x64-%s.distro" % (build, date)
        profile_name = "ent-%s-server-x64-%s-kvm-libvirt.profile" % (build, date)
        kickstart_name = "ent-ks-%s-server-x64-%s-kvm-libvirt.cfg" % (build, date)
        distro_file = kickstart_repo_dir + "/distros/" + distro_name
        profile_file = kickstart_repo_dir + "/profiles" + profile_name
        kickstart_file = kickstart_repo_dir + "/kickstarts/libvirt/RHEL%s/" % self.__get_rhel_version(kickstart_name) + kickstart_name 
        self.__check_git_repo()
        self.__check_distro(distro_file)
        self.__create_kickstart(compose, kickstart_file)
        self.__create_profile(profile_file, distro_name, kickstart_name)
        if self.__get_rhel_version(compose) == 5:
            profile_xen_name = "ent-%s-server-x64-%s-xen-libvirt.profile" % (build, date)
            profile_xen_file = kickstart_repo_dir + "/profiles" + profile_xen_name
            kickstart_xen_name = "ent-ks-%s-server-x64-%s-kvm-libvirt.cfg" % (build, date)
            kickstart_xen_file = kickstart_repo_dir + "/kickstarts/libvirt/RHEL%s/" % self.__get_rhel_version(kickstart_xen_name) + kickstart_xen_name
            self.__create_kickstart(compose, kickstart_xen_file)
            self.__create_profile(profile_xen_file, distro_name, kickstart_xen_name)
            self.__git_push(profile_xen_file, kickstart_xen_file)
        self.__git_push(profile_file, kickstart_file)

    def __check_git_repo(self):
        if not self.__check_path_exist(kickstart_repo_dir):
            logger.info("git repo not exist, cloning now ...")
            cmd = "git clone git+ssh://git@qe-git.englab.nay.redhat.com/~/repo/virt-qe/repo"
            self.git_run(cmd)
#         cmd = "pushd /root/workspace/entitlement/utils/tools/shell/repo/ && git pull && popd"
        cmd = "git pull"
        self.git_run(cmd, kickstart_repo_dir)

    def __check_distro(self, distro_name):
        # will add time out, if fail, add distro
        while not self.__check_file_exist(distro_name):
            logger.info("distro_name %s not exist yet, waiting 1 minute ..." % distro_name)
            time.sleep(60)

    def __get_rhel_version(self, file_name):
        if "RHEL5" in file_name:
            return 5
        elif "RHEL6" in file_name:
            return 6
        elif "RHEL6" in file_name:
            return 7

    def __create_kickstart(self, compose, kickstart_file):
        if "xen" in kickstart_file:
            sample_kickstart = "ent-ks-rhel5-xen-sample.cfg"
        else:
            sample_kickstart = "ent-ks-rhel%s-kvm-sample.cfg" % self.__get_rhel_version(compose)
#         "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/RHEL5.11-Server-20140625.0/tree-x86_64"
#         "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/RHEL6.5-20131213.0/6.5/Server/x86_64/os/"
#         "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/RHEL-7.0-20140507.0/compose/Server/x86_64/os/"
        compose = "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/RHEL5.11-Server-20140625.0/tree-x86_64/"
        cmd = "sed 's/url --url=.*/url --url=%s/g' 's/baseurl=.*/baseurl=%s/g' %s" % (compose, compose, dir_sample_kickstart + "/" + sample_kickstart)
        self.run(cmd)

    def __create_profile(self, profile_file, distro_name, kickstart_name):
        if not self.__check_file_exist(profile_file):
            cmd = ('cat <<EOF > %s\n'
                '[General]\n'
                'distro = %s\n'
                'kickstart = libvirt/RHEL%s/%s\n'
                'EOF' % (profile_file, distro_name, self.__get_rhel_version(distro_name), kickstart_name)
                )
            logger.info("Created profile: %s" % profile_file)
            self.run(cmd)

    def __git_push(self, profile_name, kickstart_name):
            cmd = "git add %s %s " % (profile_name, kickstart_name)
            self.run(cmd)
            cmd = "git commit -m 'Auto add virt-who kickstart file: %s %s' " % (profile_name, kickstart_name)
            self.run(cmd)
            cmd = "git push" % (profile_name, kickstart_name)
            # self.git_run(cmd, kickstart_repo_dir)

    def __check_file_exist(self, file_name):
        return os.path.isfile(file_name)

    def __check_path_exist(self, path_name):
        return os.path.exists(path_name)

if __name__ == "__main__":
    virt_who_kick = VirtWhoKickstart().create("RHEL6.5-20131213.0")
#     sam_command.add_sam_repo("SAM-1.4.0-RHEL-6-20140512.0")

