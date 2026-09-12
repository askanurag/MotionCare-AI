import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.operating_curve import operating_curve
        r=operating_curve([0,1],[.2,.8],[.1,.5,.9]);self.assertEqual(list(r.positive_rate),[1.,.5,0.])
        with self.assertRaises(ValueError):operating_curve([0,1],[.2,.8],[2])

if __name__=="__main__":unittest.main()
