from utils import *
from testcases.rhsmgui.rhsmguibase import RHSMGuiBase
from testcases.rhsmgui.rhsmguilocator import RHSMGuiLocator
from testcases.rhsmgui.rhsmconstants import RHSMConstants
from utils.exception.failexception import FailException

class tc_ID189605_GUI_service_level_should_shown_correctly(RHSMGuiBase):

    def run(self):
        case_name = self.__class__.__name__
        logger.info("========== Begin of Running Test Case %s ==========" % self.__class__.__name__)
        try:
            try:
                username = RHSMConstants().get_constant("username")
                password = RHSMConstants().get_constant("password")
                self.open_subscription_manager()
                self.register_and_autosubscribe_in_gui(username, password)
                servicelevel = RHSMConstants().get_constant("servicelevel")
                self.set_service_level(servicelevel)
                self.click_preferences_menu()
                if self.check_object_exist("system-preferences-dialog", "service-level-" + servicelevel.lower() + "-combobox"):
                    logger.info("It's successful to check service_level_should_shown_correctly.")
                else:
                    raise FailException("Test Failed - Failed to check service_level_should_shown_correctly!")
                return 0
            except Exception, e:
                logger.error("Test Failed - ERROR Message:" + str(e))
                return -1
        finally:
            self.capture_image(case_name)
            self.restore_gui_environment()
            logger.info("========== End of Running Test Case: %s ==========" % case_name)

if __name__ == "__main__":
    tc_ID189605_GUI_service_level_should_shown_correctly().run()
