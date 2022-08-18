import transposition
import unittest

class railFence(unittest.TestCase):
    def testEn(self):
        self.assertEqual(transposition.railFenceEn("1234567890", 2, False),"1357924680")
        self.assertEqual(transposition.railFenceEn("1234567890", 3, False), "1592468037")
        self.assertEqual(transposition.railFenceEn("1234567890", 4, True), ["17","268","359","40"])
        self.assertEqual(transposition.railFenceEn("1234567890", 5, True), ["19","280","37","46","5"])

    def testDe(self):
        self.assertEqual(transposition.railFenceDe("1357924680", 2),"1234567890")
        self.assertEqual(transposition.railFenceDe("1592468037", 3), "1234567890")
        self.assertEqual(transposition.railFenceDe("1726835940", 4), "1234567890")
        self.assertEqual(transposition.railFenceDe("1928037465", 5), "1234567890")        


if __name__ == "__main__":
    unittest.main()