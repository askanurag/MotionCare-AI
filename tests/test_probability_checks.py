import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.probability_checks import check_probabilities
        np.testing.assert_array_equal(check_probabilities([0,.5,1],3),[0,.5,1])
        for value in [[-1],[np.nan],[1.01],[]]:
            with self.assertRaises(ValueError):check_probabilities(value)

if __name__=="__main__":unittest.main()
