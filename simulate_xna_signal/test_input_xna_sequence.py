import unittest
import pandas as pd
from unittest.mock import patch
from simulate_xna_signal import input_xna_sequence

import unittest
from simulate_xna_signal import input_xna_sequence

class TestInputXnaSequenceFunction(unittest.TestCase):

    def test_input_xna_sequence(self):
        # Test case to check if input_xna_sequence returns the expected KXmers list

        # Arrange
        expected_kxmers = ['ATAG', 'TAGC', 'AGCT', 'GCTG', 'CTGA', 'TGAC', 'TGAC']

        # Act
        # use the unittest.mock module to simulate user input
        with unittest.mock.patch('builtins.input', return_value='ATAGCTGAC'):
            result = input_xna_sequence()

        # Assert
        self.assertEqual(result, expected_kxmers, msg="The generated KXmers list does not match the expected result")

if __name__ == '__main__':
    unittest.main()
