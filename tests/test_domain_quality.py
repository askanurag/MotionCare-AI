import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_quality import recording_quality
        r=recording_quality(self.record);self.assertTrue(isinstance(r,dict));self.assertTrue(all(v is not None for v in r.values()))

if __name__=="__main__":unittest.main()
