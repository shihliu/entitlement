'''
commands to create virt-who kickstart file
make sure repo/distros exist, add repo/profiles/ and repo/kickstarts/libvirt/RHEL[5,6,7]/ 
'''
import os, time
from utils import logger
from utils.tools.shell.command import Command

runtime_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "runtime/"))
kickstart_repo_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "runtime/repo/"))
dir_sample_kickstart = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "data/kickstart/"))

class VirtWhoKickstart(Command):

    def create(self, compose):
        build, date, distro_name = self.__get_distro_name(compose)
        profile_name = "ent-%s-server-x64-%s-kvm-libvirt.profile" % (build, date)
        kickstart_name = "ent-ks-%s-server-x64-%s-kvm-libvirt.cfg" % (build, date)
        distro_file = kickstart_repo_dir + "/distros/" + distro_name
        profile_file = kickstart_repo_dir + "/profiles/" + profile_name
        kickstart_file = kickstart_repo_dir + "/kickstarts/libvirt/RHEL%s/" % self.__get_rhel_version(kickstart_name) + kickstart_name 
        self.__check_git_repo()
        self.__check_distro(distro_file)
        self.__create_kickstart(compose, kickstart_file)
        self.__create_profile(profile_file, distro_name, kickstart_name)
        if self.__get_rhel_version(compose) == 5:
            profile_xen_name = "ent-%s-server-x64-%s-xen-libvirt.profile" % (build, date)
            profile_xen_file = kickstart_repo_dir + "/profiles/" + profile_xen_name
            kickstart_xen_name = "ent-ks-%s-server-x64-%s-xen-libvirt.cfg" % (build, date)
            kickstart_xen_file = kickstart_repo_dir + "/kickstarts/libvirt/RHEL%s/" % self.__get_rhel_version(kickstart_xen_name) + kickstart_xen_name
            self.__create_kickstart(compose, kickstart_xen_file)
            self.__create_profile(profile_xen_file, distro_name, kickstart_xen_name)
            self.__git_push(profile_xen_file, kickstart_xen_file)
        self.__git_push(profile_file, kickstart_file)

    def __get_distro_name(self, compose):
#         RHEL6.5-20131213.0
#         RHEL6u5-Server-x64-20131213.0.distro
#         RHEL-7.0-20140507.0
#         RHEL-7u0-Server-x64-20140507.0.distro
#         RHEL5.11-Server-20140625.0
#         RHEL5u11-Server-x86_64-20140625.0.distro
        if self.__get_rhel_version(compose) == 5:
            build = compose.split("-")[0].replace(".", "u")
            date = compose.split("-")[2]
            return build, date, "%s-Server-x86_64-%s.distro" % (build, date)
        elif self.__get_rhel_version(compose) == 6:
            build = compose.split("-")[0].replace(".", "u")
            date = compose.split("-")[1]
            return build, date, "%s-Server-x64-%s.distro" % (build, date)
        elif self.__get_rhel_version(compose) == 7:
            build = compose.split("-")[0] + "-" + compose.split("-")[1].replace(".", "u")
            date = compose.split("-")[2]
            return compose.split("-")[0] + compose.split("-")[1].replace(".", "u"), date, "%s-Server-x64-%s.distro" % (build, date)

    def __get_build_name(self, compose):
        if self.__get_rhel_version(compose) == 5:
            build = compose.split("-")[0].replace(".", "u")
            date = compose.split("-")[2]
            return "%s-Server-x86_64-%s.distro" % (build, date)
        elif self.__get_rhel_version(compose) == 6:
            build = compose.split("-")[0].replace(".", "u")
            date = compose.split("-")[1]
            return "%s-Server-x64-%s.distro" % (build, date)
        elif self.__get_rhel_version(compose) == 7:
            build = compose.split("-")[0] + "-" + compose.split("-")[1].replace(".", "u")
            date = compose.split("-")[2]
            return "%s-Server-x64-%s.distro" % (build, date)

    def __check_git_repo(self):
        if not self.__check_path_exist(kickstart_repo_dir):
            logger.info("git repo not exist, cloning now ...")
            cmd = "git clone git+ssh://git@qe-git.englab.nay.redhat.com/~/repo/virt-qe/repo"
            if not self.__check_path_exist(runtime_dir):
                self.__create_path(runtime_dir)
            self.git_run(cmd, runtime_dir)
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
        elif "RHEL7" or "RHEL-7" in file_name:
            return 7

    def __create_kickstart(self, compose, kickstart_file):
        if "xen" in kickstart_file:
            sample_kickstart = "ent-ks-rhel5-xen-sample.cfg"
        else:
            sample_kickstart = "ent-ks-rhel%s-kvm-sample.cfg" % self.__get_rhel_version(compose)
#             RHEL6.5-20131213.0
        if self.__get_rhel_version(compose) == 5:
            compose_url = "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/%s/tree-x86_64" % compose
        elif self.__get_rhel_version(compose) == 6:
            compose_url = "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/%s/%s/Server/x86_64/os/" % (compose, self.__get_rhel_version(compose))
        elif self.__get_rhel_version(compose) == 7:
            compose_url = "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/%s/compose/Server/x86_64/os/" % compose
#         "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/RHEL5.11-Server-20140625.0/tree-x86_64"
#         "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/RHEL6.5-20131213.0/6/Server/x86_64/os/"
#         "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/RHEL-7.0-20140507.0/compose/Server/x86_64/os/"
        cmd = "sed -e 's#auto-rhel-compose-url#%s#g' %s > %s" % (compose_url, dir_sample_kickstart + "/" + sample_kickstart, kickstart_file)
        logger.info("Created kickstart: %s" % kickstart_file)
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
            cmd = "git push"
            self.git_run(cmd, kickstart_repo_dir)

    def __check_file_exist(self, file_name):
        return os.path.isfile(file_name)

    def __check_path_exist(self, path_name):
        return os.path.exists(path_name)

    def __create_path(self, path_name):
        os.makedirs(path_name)

if __name__ == "__main__":
#     virt_who_kick = VirtWhoKickstart().create("RHEL6.5-20131213.0")
#     virt_who_kick = VirtWhoKickstart().create("RHEL-7.0-20140507.0")
    virt_who_kick = VirtWhoKickstart().create("RHEL5.11-Server-20140625.0")
#     sam_command.add_sam_repo("SAM-1.4.0-RHEL-6-20140512.0")

