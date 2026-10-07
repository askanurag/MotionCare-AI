import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.data_fingerprint import file_digest,manifest
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x';p.write_text('abc');a=file_digest(p);self.assertEqual(len(a),64);p.write_text('abcd');self.assertNotEqual(a,file_digest(p));self.assertEqual(manifest([p])[0]['bytes'],4)

if __name__=="__main__":unittest.main()
