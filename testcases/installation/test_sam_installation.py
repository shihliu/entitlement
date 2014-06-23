from utils import *
from utils.installation.saminstall import SAMInstall

class Test_Sam_Installation(unittest.TestCase):


    def setUp(self):
        SAMInstall().start()


    def tearDown(self):
        pass


    def testName(self):
        self.assertEqual(1, 1, "test")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
