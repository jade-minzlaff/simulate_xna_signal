import unittest
import pandas as pd
from unittest.mock import patch
from simulate_xna_signal import xplot

class TestXPlotFunction(unittest.TestCase):

    def test_xplot_generates_list(self):
        # Test case to check if xplot generates a list

        # Arrange
        kxmers = [ATGC, TGCA, GTCG, TCGA, TCGA]  # fake list for example

        # Act
        result = xplot(kxmers)

        # Assert
        self.assertIsInstance(result, list, msg="Output is not a list")
        self.assertGreater(len(result), 0, msg="Output list is empty")

if __name__ == '__main__':
    unittest.main()