"""
Defines various constants
"""
import os

# configure module
SAM_INSTALLATION_CONF = "sam_installation.conf"
RHEL_INSTALLATION_CONF = "rhel_installation.conf"
VIRTWHO_KICKSTART_CONF = "virtwho_kickstart.conf"
OPENSTACK_INSTALLATION_CONF = "openstack_installation.conf"

# log module
LOGGER_NAME = "entitlement"
LOGGER_FILE = "entitlement.log"

# build location
SAM_BUILD_URL = "http://download.devel.redhat.com/devel/candidate-trees/SAM/"
RHEL_BUILD_URL = "http://download.englab.nay.redhat.com/pub/rhel/rel-eng/"

# path environments
DATA_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "data/"))
RUNTIME_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "runtime/"))
BEAKER_JOBS_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "data/beakerjobs/"))


def get_build_tree(product_name):
    build_url = ""
    product_name = product_name.upper()
    if product_name.startswith("SAM"):
        build_url = SAM_BUILD_URL
    elif product_name.startswith("RHEL"):
        build_url = RHEL_BUILD_URL
    else:
        # logger.error("Unknown product name : %s " % product_name)
        build_url = "Unknown"
    return build_url


# FILTER_TYPE = {'include': "Include",
#                'exclude': "Exclude"}
