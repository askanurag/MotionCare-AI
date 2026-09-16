import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_labels import segment_label
        from healthcare_ai.domain_windows import segments
        labels=[segment_label(p) for p in segments(self.record)];self.assertTrue(set(labels)<={0,1});self.assertEqual(set(labels),{0,1})

if __name__=="__main__":unittest.main()
