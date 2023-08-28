import unittest
from main import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.path = r'test_data.csv'

    def test_data_len(self):
        data = main(self.path, '2S', 10)
        data2 = main(self.path, '2T', 10)
        data3 = main(self.path, '2H', 10)
        data4 = main(self.path, '2W', 10)
        assert len(data) == 3434875
        assert len(data2) == 57249
        assert len(data3) == 955
        assert len(data4) == 7

    def test_ohcl(self):
        data = main(self.path, '1T', 10)
        assert data.Open.iat[0] == 1875.979748793
        assert data.High.iat[0] == 1876.7313482702
        assert data.Low.iat[0] == 1875.979748793
        assert data.Close.iat[0] == 1876.7313482702

    def test_ema(self):
        data = main(self.path, '1T', 10)
        assert data.MA.iat[0] == 1876.3555485316


