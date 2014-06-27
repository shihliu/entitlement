from utils.tools.shell.remotesh import RemoteSH
from utils.tools.shell.localsh import LocalSH

class Command(object):
    remote_ip = username = password = None
    def __init__(self, remote_ip=None, username=None, password=None):
        if remote_ip != "" and remote_ip != None:
            self.remote_ip = remote_ip
            self.username = username
            self.password = password

    def run(self, cmd, timeout=None):
        if self.remote_ip == None:
            # (ret, output) = commands.getstatusoutput(cmd, timeout)
            ret, output = LocalSH.local_run(cmd, timeout)
        else:
            ret, output = RemoteSH.remote_run(cmd, self.remote_ip, self.username, self.password, timeout)
#             ret, output = RemoteSH.run_pexpect(cmd, self.remote_ip, self.username, self.password, timeout)
        return ret, output

    def remote_put(self, from_path, to_path):
        RemoteSH.remote_put(self.remote_ip, self.username, self.password, from_path, to_path)

    def fork_run(self, cmd, timeout=None):
        pass
