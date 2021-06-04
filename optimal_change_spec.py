# Write your unit tests here!
import unittest
from optimal_change import optimal_change

class OptimalChangeTestCase(unittest.TestCase):
    def test_optimal_change(self):
        actual_output1 = optimal_change(62.13, 100)
        expected_output1 = "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."
        #####################################################################
        actual_output2 = optimal_change(62.13, 100)
        expected_output2 = "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."
        #####################################################################
        self.assertEqual(actual_output1, expected_output1)
        self.assertEqual(actual_output2, expected_output2)
    

if __name__ == "__main__":
    unittest.main()
