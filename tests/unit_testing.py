import unittest
import sys
sys.path.append("./")

from src.utils.preprocess import *


class TestPreprocess(unittest.TestCase):
    def test_remove_special_char(self):
        test_cases = [
            {"message": "abc", "expect_output": "abc"},
            {"message": "Abc", "expect_output": "Abc"},
            {"message": "abc😆😆😆", "expect_output": "abc "},
            {"message": "I'm fine !!!!", "expect_output": "I'm fine "}
        ]

        for test_case in test_cases:
            output = remove_special_char(test_case["message"])
            self.assertEqual(output, test_case["expect_output"])

    def test_remove_urls(self):
        test_cases = [
            {"message": "abc", "expect_output": "abc"},
            {
                "message": """learn more from https://dev.to/kalkwst/ and https://github.com/PROMJODD/""", 
                "expect_output": "learn more from and "
            }
        ]

        for test_case in test_cases:
            output = remove_url(test_case["message"])
            self.assertEqual(output, test_case["expect_output"])


if __name__ == "__main__":
   unittest.main()