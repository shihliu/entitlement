import time, os, signal
import subprocess
from utils import logger

class LocalSH(object):
    """
    Run shell in local machine via subprocess
    """

    @classmethod
    def local_run(self, cmd, timeout=None):
        """
        Executes SSH command on local machine.
        """
        logger.info(">>>Local Run: %s" % cmd)
#         retcode, stdout = self.run_subprocess(cmd, timeout)
        retcode, stdout = self.run_subprocess(cmd, timeout)
        logger.info("<<<Return Code: %s" % retcode)
        logger.info("<<<Output:\n%s" % stdout)
        return retcode, stdout

    @classmethod
    def run_subprocess(self, cmd, timeout=None):
        """
        Executes SSH command on local machine.
        if running cmd with large bulk of output, it's easy to be blocked
        """
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        # if timeout is not set wait for process to complete
        if timeout == None:
            retcode = process.wait()
            stdout, stderr = process.communicate()
        else:
            terminate_time = time.time() + timeout
            while process.poll() == None:
                logger.debug("Run command, wait 1 minute ...")
                time.sleep(1)
                if terminate_time < time.time():
                    # starting 2.6 subprocess has a kill() method which is preferable
                    logger.debug("Kill process, return -1 ...")
                    retcode = -1
                    stdout = "Command terminated due to timeout ..."
                    process.kill()
            retcode = process.wait()
            stdout, stderr = process.communicate()
#                 os.kill(process.pid, signal.SIGKILL)
#                 raise OSError("Process timeout has been reached")
#             retcode = process.returncode
        return retcode, stdout

    @classmethod
    def run_popen(self, cmd, timeout=None):
        import os
        output = os.popen(cmd)
        print output
    @classmethod
    def run_system(self, cmd, timeout=None):
        import os
        os.system(cmd)
    @classmethod
    def run_commands(self, cmd, timeout=None):
        '''not blocking method'''
        import commands
        retcode, stdout = commands.getstatusoutput(cmd)
        return retcode, stdout
        
# child1 = subprocess.Popen(["dir","/w"], stdout=subprocess.PIPE,shell=True)  
# child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=subprocess.PIPE,shell=True)  
# out = child2.communicate()  

if __name__ == "__main__":
#     LocalSH.local_run("/usr/bin/virt-install --network=bridge:br0 --initrd-inject=/root/workspace/entitlement/data/kickstart/unattended/rhel-server-6-series.ks --extra-args \"ks=file:/rhel-server-6-series.ks\" --name=AUTO-SAM-1.4.0-RHEL-6-20140512.0 --disk path=/home/auto-imgs/AUTO-SAM-1.4.0-RHEL-6-20140512.0.img,size=20 --ram 2048 --vcpus=2 --check-cpu --accelerate --hvm --location=http://download.englab.nay.redhat.com/pub/rhel/released/RHEL-6/6.5/Server/x86_64/os/ ", 10)
    LocalSH.local_run("ifconfig", 20)
