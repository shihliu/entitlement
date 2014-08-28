from utils import *
from testcases.rhsmgui.rhsmguibase import RHSMGuiBase
from testcases.rhsmgui.rhsmguilocator import RHSMGuiLocator
from testcases.rhsmgui.rhsmconstants import RHSMConstants

class tc_ID000000_GUI_list_all_objects(RHSMGuiBase):

    def run_tc_ID000000_GUI_list_all_objects(self):
        case_name = self.__class__.__name__
        logger.info("========== Begin of Running Test Case %s ==========" % case_name)
        try:
            try:
                # open subscription-manager-gui
                self.open_subscription_manager()
                self.list_objects("main-window")
            except Exception, e:
                logger.error("Test Failed - ERROR Message:" + str(e))
        finally:
            self.capture_image(case_name)
            self.restore_gui_environment()
            logger.info("========== End of Running Test Case: %s ==========" % case_name)

if __name__ == "__main__":
    tc_ID000000_GUI_list_all_objects().run_tc_ID000000_GUI_list_all_objects()
