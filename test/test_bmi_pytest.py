import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from bmi import bmi, category

def test_bmi():
    assert bmi(70, 1.75) == 22.86

def test_category():
    assert category(22.86) == "Normal"
    assert category(30) == "Obese"
