from utils.configs import Configs

class Install(object):
    '''
    Abstract class, template for installation
    '''

    def __init__(self, conf_file_name):
        '''
        Parse configure file
        '''
        Configs(conf_file_name)

    def install(self):
        self.check_build()
        self.install_host()
        self.install_guest()
        self.install_product()


    def check_build(self):
        raise NotImplementedError, "Cannot call abstract method"

    def install_host(self):
        raise NotImplementedError, "Cannot call abstract method"

    def install_guest(self):
        raise NotImplementedError, "Cannot call abstract method"

    def install_product(self):
        raise NotImplementedError, "Cannot call abstract method"
