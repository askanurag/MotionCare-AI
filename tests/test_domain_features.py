import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_features import segment_features
        from healthcare_ai.domain_windows import segments
        from healthcare_ai.domain_contract import validate_recording
        from healthcare_ai.settings import FEATURES
        r=segment_features(segments(self.record)[0],validate_recording(self.record));self.assertEqual(list(r),FEATURES);self.assertTrue(np.isfinite(list(r.values())).all())

if __name__=="__main__":unittest.main()
