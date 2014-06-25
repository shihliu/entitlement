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
        logger.info(">>> %s" % cmd)
        retcode, stdout = self.run_subprocess(cmd, timeout)
        logger.info("<<<\n%s" % stdout)
        return retcode, stdout

    @classmethod
    def run_subprocess(self, cmd, timeout=None):
        """
        Executes SSH command on local machine.
        """
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        stdout, stderr = process.communicate(timeout=None)
        retcode = process.poll()
        return retcode, stdout

# child1 = subprocess.Popen(["dir","/w"], stdout=subprocess.PIPE,shell=True)  
# child2 = subprocess.Popen(["wc"], stdin=child1.stdout,stdout=subprocess.PIPE,shell=True)  
# out = child2.communicate()  

if __name__ == "__main__":
    LocalSH.local_run("ifconfig")
