import unittest
from reference_manual import md_heading, csv_heading, md_format_line, csv_format_line


class TestReferenceManual(unittest.TestCase):
    def test_md_heading(self):
        self.assertEqual(md_heading(), "| Pair number | Major Color | Minor Color |\n| --- | --- | --- |")

    def test_csv_heading(self):
        self.assertEqual(csv_heading(), "Pair number,Major Color,Minor Color")

    def test_md_format_line(self):
        self.assertEqual(md_format_line(1, "White", "Blue"), "| 1 | White | Blue |")

    def test_csv_format_line(self):
        self.assertEqual(csv_format_line(1, "White", "Blue"), "1,White,Blue")


if __name__ == "__main__":
    unittest.main()
