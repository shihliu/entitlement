from utils.configs import Configs
from utils import logger
from utils.tools.xmlparser import buildxml
from utils.tools.htmlparser import buildparser

class Install(object):
    '''
    Abstract class, template for installation
    '''
    conf_file_name = ""
    product_name = ""

    def __init__(self):
        '''
        Parse configure file
        '''
        Configs(self.conf_file_name)

    def start(self):
        new_build = self.check_build()
        if new_build == "No New Build":
            logger.info("No %s new build available yet, just exit ..." % self.product_name) 
        else:
            logger.info("Found %s new build %s, begin installing ..." % (self.product_name, new_build)) 
            self.install_host()
            self.install_guest()
            self.install_product()

#     def new_build_check(self, product_name):
#         # check the last build in html, if not in xml file then it's a new build
#         last_build = buildparser.build_list(product_name.upper())[-1]
#         if not last_build in buildxml.get_builds(product_name):
#             return last_build
#         else:
#             return "No New Build"

    def check_build(self):
        # check the last build in html, if not in xml file then it's a new build
        last_build = buildparser.build_list(self.product_name.upper())[-1]
        if not last_build in buildxml.get_builds(self.product_name.lower()):
            buildxml.add_build(self.product_name.lower(), last_build)
            return last_build
        else:
            return "No New Build"

    def install_host(self):
        raise NotImplementedError, "Cannot call abstract method"

    def install_guest(self):
        raise NotImplementedError, "Cannot call abstract method"

    def install_product(self):
        raise NotImplementedError, "Cannot call abstract method"
