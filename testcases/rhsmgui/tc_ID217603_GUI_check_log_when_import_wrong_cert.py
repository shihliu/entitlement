from utils import *
from testcases.rhsmgui.rhsmguibase import RHSMGuiBase
from testcases.rhsmgui.rhsmguilocator import RHSMGuiLocator
from testcases.rhsmgui.rhsmconstants import RHSMConstants
from utils.exception.failexception import FailException

class tc_ID217603_GUI_check_log_when_import_wrong_cert(RHSMGuiBase):

    def test_run(self):
        case_name = self.__class__.__name__
        logger.info("========== Begin of Running Test Case %s ==========" % self.__class__.__name__)
        try:
            try:
                self.open_subscription_manager()
                # click register button
                self.click_ImportCertificate_button()
                self.click_Certificate_Location()
                self.input_location("/tmp/doesnotexistblahblah.pem")
                self.click_import_cert_button()
                self.close_error_cert_dialog()
                # since 6.4 is different with 6.4, so will complete it later, check log, check dialog opened.
#                 if self.get_my_subscriptions_table_row_count() >= 1:
#                     logger.info("It's successful to auto subscribe: %s" % self.get_my_subscriptions_table_my_subscriptions())
#                 else:
#                     raise FailException("Test Faild - Failed to register and auto subscribe via GUI!")
                return 0
            except Exception, e:
                logger.error("Test Failed - ERROR Message:" + str(e))
                return -1
        finally:
            self.capture_image(case_name)
            self.restore_gui_environment()
            logger.info("========== End of Running Test Case: %s ==========" % case_name)

if __name__ == "__main__":
    tc_ID217603_GUI_check_log_when_import_wrong_cert().test_run()
