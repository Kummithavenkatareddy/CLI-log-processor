import os
import unittest

from src.Infrastructure.file_reader import read_lines


class TestFileReader(unittest.TestCase):
    def test_read_lines_sample(self):
        path = os.path.join(os.getcwd(), "sample.log")
        lines = list(read_lines(path))
        self.assertGreater(len(lines), 0)
        # check that first line contains expected snippet
        self.assertIn("Application started", lines[0])

    def test_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            list(read_lines("nonexistent_file_12345.log"))


if __name__ == "__main__":
    unittest.main()
