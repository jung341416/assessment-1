# Write your unit tests here!
import unittest
from optimal_change import optimal_change

class OptimalChangeTestCase(unittest.TestCase):
    def test_optimal_change(self):
        actual_output1 = optimal_change(62.13, 100)
        expected_output1 = "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."
        ##################################################################################################################################################################
        actual_output2 = optimal_change(31.51, 50)
        expected_output2 = "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
        ##################################################################################################################################################################
        actual_output3 = optimal_change(92.25, 100)
        expected_output3 = "The optimal change for an item that costs $92.25 with an amount paid of $100 is 1 $5 bill, 2 $1 bills, and 3 quarters."
        ##################################################################################################################################################################
        actual_output4 = optimal_change(91.5, 100)
        expected_output4 = "The optimal change for an item that costs $91.5 with an amount paid of $100 is 1 $5 bill, 3 $1 bills, and 2 quarters."
        ##################################################################################################################################################################
        actual_output5 = optimal_change(62.13, 100)
        expected_output5 = "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."
        ##################################################################################################################################################################
        actual_output6 = optimal_change(0.1, 1)
        expected_output6 = "The optimal change for an item that costs $0.1 with an amount paid of $1 is 3 quarters, 1 dime, and 1 nickle."
        ##################################################################################################################################################################
        actual_output7 = optimal_change(20, 100)
        expected_output7 = "The optimal change for an item that costs $20 with an amount paid of $100 is 4 $20 bills."
        actual_output8 = optimal_change(0.05, 0.1)
        expected_output8 = "The optimal change for an item that costs $0.05 with an amount paid of $0.1 is 1 nickle."
        self.assertEqual(actual_output1, expected_output1)
        self.assertEqual(actual_output2, expected_output2)
        self.assertEqual(actual_output3, expected_output3)
        self.assertEqual(actual_output4, expected_output4)
        self.assertEqual(actual_output5, expected_output5)
        self.assertEqual(actual_output6, expected_output6)
        self.assertEqual(actual_output7, expected_output7)
        self.assertEqual(actual_output8, expected_output8)

if __name__ == "__main__":
    unittest.main()
