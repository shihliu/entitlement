from utils import *
from testcases.rhsmgui.rhsmguibase import RHSMGuiBase
from testcases.rhsmgui.rhsmguilocator import RHSMGuiLocator
from testcases.rhsmgui.rhsmconstants import RHSMConstants

class tc_ID115150_GUI_register(RHSMGuiBase):

    def run_tc_ID115150_GUI_register(self):
        case_name = self.__class__.__name__
        logger.info("========== Begin of Running Test Case %s ==========" % self.__class__.__name__)
        try:
            try:
                username = RHSMConstants().get_constant("username")
                password = RHSMConstants().get_constant("password")
                # open subscription-manager-gui
                self.open_subscription_manager()
                self.check_consumer_cert_files(exist=False)
                # click register button
                self.click_register_button()
                self.click_dialog_next_button()
                self.input_username(username)
                self.input_password(password)
                self.check_manual_attach_checkbox()
                self.click_dialog_register_button_without_autoattach()
                if self.check_consumer_cert_files():
                    logger.info("It's successful to check certificate files are dropped into /etc/pki/consumer")
                else:
                    logger.error("Test Faild - Failed to check certificate files are dropped into /etc/pki/consumer")
            except Exception, e:
                logger.error("Test Failed - ERROR Message:" + str(e))
        finally:
            self.capture_image(case_name)
            self.restore_gui_environment()
            logger.info("========== End of Running Test Case: %s ==========" % case_name)

if __name__ == "__main__":
    tc_ID115150_GUI_register().run_tc_ID115150_GUI_register()
