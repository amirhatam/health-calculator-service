import unittest
# from src.health_utils import calculate_bmi, calculate_bmr
from health_utils import calculate_bmi, calculate_bmr


class TestHealthCalculations(unittest.TestCase):
    def test_bmi_normal_case(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, delta=0.1)

    def test_bmi_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_bmi(0, 70)

    def test_bmr_male(self):
        expected = 88.362 + (13.397*70) + (4.799*175) - (5.677*30)
        self.assertAlmostEqual(calculate_bmr(1.75, 70, 30, 'male'), expected, delta=0.1)

    def test_bmr_invalid_gender(self):
        with self.assertRaises(ValueError):
            calculate_bmr(1.75, 70, 30, 'invalid')

if __name__ == '__main__':
    unittest.main()
