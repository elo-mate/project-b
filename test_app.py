"""Tests for Project B."""
import unittest
from app import process_data, filter_items


class TestProcessData(unittest.TestCase):
    def test_empty_list(self):
        result = process_data([])
        self.assertEqual(result["count"], 0)

    def test_basic_stats(self):
        result = process_data([10, 20, 30])
        self.assertEqual(result["count"], 3)
        self.assertEqual(result["total"], 60)
        self.assertEqual(result["average"], 20)


class TestFilterItems(unittest.TestCase):
    def test_min_filter(self):
        result = filter_items([1, 5, 10, 15], min_value=5)
        self.assertEqual(result, [5, 10, 15])

    def test_max_filter(self):
        result = filter_items([1, 5, 10, 15], max_value=10)
        self.assertEqual(result, [1, 5, 10])


if __name__ == "__main__":
    unittest.main()
