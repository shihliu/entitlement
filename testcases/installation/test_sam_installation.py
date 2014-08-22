from utils import *
from beaker.bksaminstall import BKSAMInstall

class Test_Sam_Installation(unittest.TestCase):


    def setUp(self):
#         SAMInstall().start()
        BKSAMInstall().start()


    def tearDown(self):
        pass


    def testName(self):
        self.assertEqual(1, 1, "test")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
