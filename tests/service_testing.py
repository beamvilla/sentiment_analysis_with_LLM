import unittest
import sys
sys.path.append("./")

from src.utils.preprocess import *


class TestPreprocess(unittest.TestCase):
    def test_remove_special_char(self):
        test_cases = [
            {"message": "abc", "expect_output": "abc"},
            {"message": "abc😆😆😆", "expect_output": "abc"},
            {"message": "I'm fine !!!!", "expect_output": "I'm fine"}
        ]

        for test_case in test_cases:
            output = remove_special_char(test_case["message"])
            self.assertEqual(output, test_case["expect_output"])


if __name__ == "__main__":
   unittest.main()