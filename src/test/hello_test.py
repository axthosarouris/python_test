import unittest
from src.main.hello import Hello
from assertpy import assert_that


class HelloTest(unittest.TestCase):

    @staticmethod
    def test_should_return_hello_test():
        hello = Hello()
        assert_that(hello.hello()).is_equal_to("Hello world")


if __name__ == '__main__':
    unittest.main()
