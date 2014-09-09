from utils import *
from testcases.rhsmgui import *

class Test_RHSM_GUI(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAll(self):
        self.regressionTest()

    def regressionTest(self):
        path = os.path.abspath(os.path.realpath(os.path.join(os.path.dirname(__file__), os.pardir, "testcases/rhsmgui/")))
        files = os.listdir(path).sort()
        case = re.compile("tc_ID", re.IGNORECASE)
        files = filter(case.search, files)
        filenameToModuleName = lambda f: os.path.splitext(f)[0]
        moduleNames = map(filenameToModuleName, files)
        sys.path.append(path)
        for testcase in moduleNames:
            obj = __import__(testcase)
            getattr(getattr(obj, testcase)(), "run")()

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
