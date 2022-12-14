import encoding
import unittest

class ceaserShift(unittest.TestCase):
    def testEn(self):
        self.assertEqual(encoding.ceaserShiftEn("012345678", 1), "123456789")
        self.assertEqual(encoding.ceaserShiftEn("123456789", -1), "012345678")
        self.assertEqual(encoding.ceaserShiftEn("Hello", 5), "Mjqqt")
        self.assertEqual(encoding.ceaserShiftEn("Hello", -3), "Ebiil")

    def testDe(self):
        self.assertEqual(encoding.ceaserShiftDe("123456789", 1), "012345678")
        self.assertEqual(encoding.ceaserShiftDe("012345678", -1), "123456789")
        self.assertEqual(encoding.ceaserShiftDe("Mjqqt", 5), "Hello")
        self.assertEqual(encoding.ceaserShiftDe("Ebiil", -3), "Hello")

class rot13(unittest.TestCase):
    def testEn(self):
        self.assertEqual(encoding.rot13En("abc"), "nop")

    def testDe(self):
        self.assertEqual(encoding.rot13De("nop"), "abc")

class atBash(unittest.TestCase):
    def testEn(self):
        self.assertEqual(encoding.atbashEn("HELLOWORLD"), "SVOOLDLIOW")
        self.assertEqual(encoding.atbashEn("helloworld"), "svooldliow")
        self.assertEqual(encoding.atbashDe("HeLlOwOrLd"), "SvOoLdLiOw")
        self.assertEqual(encoding.atbashEn("_+!@123"), "_+!@123")
        self.assertEqual(encoding.atbashEn("a!b2$c"), "z!y2$x")

    def testDe(self):
        self.assertEqual(encoding.atbashDe("SVOOLDLIOW"), "HELLOWORLD")
        self.assertEqual(encoding.atbashDe("svooldliow"), "helloworld")
        self.assertEqual(encoding.atbashDe("SvOoLdLiOw"), "HeLlOwOrLd")
        self.assertEqual(encoding.atbashDe("_+!@123"), "_+!@123")
        self.assertEqual(encoding.atbashDe("z!y2$x"), "a!b2$c")


if __name__ == "__main__":
    unittest.main()