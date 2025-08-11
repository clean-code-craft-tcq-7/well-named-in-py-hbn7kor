import unittest
from colormap import color_pair_to_string, get_color_from_pair_number, get_pair_number_from_color


class TestColorMap(unittest.TestCase):
    def test_color_pair_to_string(self):
        self.assertEqual(color_pair_to_string("White", "Brown"), "White Brown")

    def test_get_color_from_pair_number(self):
        self.assertEqual(get_color_from_pair_number(4), ("White", "Brown"))
        self.assertEqual(get_color_from_pair_number(5), ("White", "Slate"))
        self.assertIsNone(get_color_from_pair_number(26))

    def test_get_pair_number_from_color(self):
        self.assertEqual(get_pair_number_from_color("Black", "Orange"), 12)
        self.assertEqual(get_pair_number_from_color("Violet", "Slate"), 25)
        self.assertEqual(get_pair_number_from_color("Red", "Orange"), 7)
        self.assertIsNone(get_pair_number_from_color("White", "Red"))


if __name__ == "__main__":
    unittest.main()
