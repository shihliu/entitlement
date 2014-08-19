from utils import *
from beaker.allinone import AllInOne

class Test_Allinone(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testName(self):
        AllInOne().start()
        self.assertEqual(1, 1, "test")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
