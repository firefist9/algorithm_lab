import unittest
from insertionSort import insertion_sort
from mergeSort import merge_sort

class SortTestCase(unittest.TestCase):
    def test_insertionSort(self):
        data = [1, 7, 4, 6, 2, 9]
        sorted_data = [1, 2, 4, 6, 7, 9]
        insertion_sort(data)
        self.assertListEqual(data, sorted_data)

    def test_mergeSort(self):
        data = [1, 7, 4, 6, 2, 9]
        sorted_data = [1, 2, 4, 6, 7, 9]
        merge_sort(data)
        self.assertListEqual(data, sorted_data)


if __name__ == '__main__':
    unittest.main()