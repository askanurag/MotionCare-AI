import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        from healthcare_ai.batch_inference import predict_batches
        from healthcare_ai.experiment import run
        from healthcare_ai.synthetic import generate
        from healthcare_ai.inference import predict
        f=generate(100);b,_=run(f);one=predict(b,f);many=predict_batches(b,f,7);np.testing.assert_allclose(one.probability,many.probability);self.assertEqual(list(one.patient_id),list(many.patient_id))

if __name__=="__main__":unittest.main()
