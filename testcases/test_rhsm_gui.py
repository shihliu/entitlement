from utils import *
from testcases.rhsmgui import *

class Test_RHSM_GUI(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAll(self):
        cases_list = ["tc_ID000000_GUI_list_all_objects", "tc_ID115150_GUI_register"]
        from testcases.rhsmgui.tc_ID000000_GUI_list_all_objects import tc_ID000000_GUI_list_all_objects
        from testcases.rhsmgui.tc_ID115150_GUI_register import tc_ID115150_GUI_register
        from testcases.rhsmgui.tc_ID115127_GUI_display_user_org import tc_ID115127_GUI_display_user_org
        self.assertEqual(tc_ID000000_GUI_list_all_objects().run(), 0, "tc_ID000000_GUI_list_all_objects")
        self.assertEqual(tc_ID115150_GUI_register().run(), 0, "tc_ID115150_GUI_register")
        self.assertEqual(tc_ID115127_GUI_display_user_org().run(), 0, "tc_ID115127_GUI_display_user_org")

    def regressionTest(self):
#         path = os.path.abspath(os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "testcases/rhsmgui/")))
#         files = os.listdir(path)
#         case = re.compile("tc_ID0000", re.IGNORECASE)
#         files = filter(case.search, files)
#         filenameToModuleName = lambda f: os.path.splitext(f)[0]
#         moduleNames = map(filenameToModuleName, files)
#         sys.path.append(path)
#         for testcase in moduleNames:
#             obj = __import__(testcase)
#             print dir(obj)
#             getattr(getattr(obj, testcase)(), "run")(self)
        pass



if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
