import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.domain_experiment import run_domain
        b,r=run_domain();self.assertFalse(r['domain_protocol']['clinical_validation']);self.assertGreater(r['test']['n'],0)

if __name__=="__main__":unittest.main()
