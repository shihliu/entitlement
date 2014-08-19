import time
from utils import logger
from utils import constants
from utils.configs import Configs
from utils.tools.htmlparser import htmlsource
from utils.tools.htmlparser.buildparser import BuildParser
from utils.tools.xmlparser.buildsparser import BuildsParser

class BeakerBase(object):
    '''
    Abstract class, template for beaker auto
    '''
    conf_file_name = ""
    product_name = ""
    confs = None

    def __init__(self):
        '''
        Parse configure file
        '''
        self.confs = Configs(self.conf_file_name)
        self.product_name = self.confs._confs["version"]

    def check_build(self):
        # check the last build from html, if not in xml file then it's a new build
        last_build = BuildParser().parse(self.product_name)[-1]
        if not last_build in BuildsParser().get_builds(self.product_name):
            BuildsParser().add_build(self.product_name, last_build)
            self.check_build_status(last_build)
            return 0, last_build.strip("/")
        else:
            return -1, last_build.strip("/")
