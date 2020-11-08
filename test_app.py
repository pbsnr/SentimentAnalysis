import unittest
import app


class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(app.analyse_text('Oldboy is a great movie'), 1)
        self.assertEqual(app.analyse_text('I hate pineapples on pizzas'), -1)
        self.assertEqual(app.analyse_text('The sky is blue'), 0)


if __name__ == '__main__':
    unittest.main()