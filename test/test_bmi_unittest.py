import unittest
import sys, os

# Add src folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from bmi import bmi, category

class TestBMI(unittest.TestCase):
    def test_bmi(self):
        self.assertEqual(bmi(70, 1.75), 22.86)

    def test_category(self):
        self.assertEqual(category(22.86), "Normal")
        self.assertEqual(category(30), "Obese")

if __name__ == "__main__":
    unittest.main()
