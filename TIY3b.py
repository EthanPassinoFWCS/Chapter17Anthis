from TIY3 import Python_Repos
import unittest


class APICallTestCase(unittest.TestCase):

    def test_status(self):
        p = Python_Repos()
        self.assertEqual(p.status_code, 200)

    def test_repo_len(self):
        p = Python_Repos()
        self.assertEqual(p.get_num_items() > 10, True)


if __name__ == '__main__':
    unittest.main()
