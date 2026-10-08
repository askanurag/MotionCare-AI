import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_windows import segments
        w=segments(self.record);self.assertGreater(len(w),1)
        with self.assertRaises(ValueError):segments(self.record,0,0)

if __name__=="__main__":unittest.main()
