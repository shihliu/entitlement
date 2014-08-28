from utils import *
from testcases.rhsmgui.rhsmguibase import RHSMGuiBase
from testcases.rhsmgui.rhsmguilocator import RHSMGuiLocator

class tc_ID000000_GUI_list_all_objects(RHSMGuiBase):

	def run_tc_ID000000_GUI_list_all_objects(self):
		logging.info("========== Begin of Running Test Case %s ==========" % __name__)
		try:
			try:
				# open subscription-manager-gui
				self.open_subscription_manager()
	# 			RHSMGuiLocator().list_objects("main-window")
	
		# 		# click register button
		# 		egu().click_register_button()
		# 		egu().click_dialog_next_button()
		# 		egu().input_username(username)
		# 		egu().input_password(password)
		# 		egu().click_dialog_register_button()
		# 		egu().click_dialog_subscribe_button()
		# 		egu().click_my_subscriptions_tab()
		# 		if egu().get_my_subscriptions_table_row_count() >= 1:
		# 			logging.info("It's successful to auto subscribe: %s" % egu().get_my_subscriptions_table_my_subscriptions())
		# 		else:
		# 			raise error.TestFail("Test Faild - Failed to list all objects!")
			except Exception, e:
				logging.error("Test Failed - error happened to list all objects:" + str(e))
		finally:
			RHSMGuiLocator().capture_image("list_all_objects")
			RHSMGuiLocator().restore_gui_environment()
			logging.info("========== End of Running Test Case: %s ==========" % __name__)
