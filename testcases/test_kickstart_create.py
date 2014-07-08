from utils import *
from utils.installation.vwkscreate import VWKSCreate

class Test_Kickstart_Create(unittest.TestCase):


    def setUp(self):
        VWKSCreate().start()


    def tearDown(self):
        pass


    def testName(self):
        self.assertEqual(1, 1, "test")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
