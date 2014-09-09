from utils import *
from testcases.rhsmgui.rhsmguibase import RHSMGuiBase
from testcases.rhsmgui.rhsmguilocator import RHSMGuiLocator
from testcases.rhsmgui.rhsmconstants import RHSMConstants
from utils.exception.failexception import FailException

class tc_ID115127_GUI_display_user_org(RHSMGuiBase):

    def test_run(self):
        case_name = self.__class__.__name__
        logger.info("========== Begin of Running Test Case %s ==========" % case_name)
        try:
            try:
                username = RHSMConstants().get_constant("username")
                password = RHSMConstants().get_constant("password")
                self.open_subscription_manager()
                self.register_and_autosubscribe_in_gui(username, password)
                self.click_view_system_facts_menu()
                self.check_org_displayed_in_facts(username, password)
                return 0
            except Exception, e:
                logger.error("Test Failed - ERROR Message:" + str(e))
                return -1
        finally:
            self.capture_image(case_name)
            self.restore_gui_environment()
            logger.info("========== End of Running Test Case: %s ==========" % case_name)

if __name__ == "__main__":
    tc_ID115127_GUI_display_user_org().test_run()
