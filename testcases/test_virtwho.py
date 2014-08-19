from utils import *
from beaker.bkvirtwho import BKvirtwho

class Test_VIRTWHO(unittest.TestCase):


    def setUp(self):
#         SAMInstall().start()
        BKvirtwho().start()


    def tearDown(self):
        pass


    def testName(self):
        self.assertEqual(1, 1, "test")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
