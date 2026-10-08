import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.event_labels import label_window
        self.assertEqual(label_window(0,4,[4]),0);self.assertEqual(label_window(4,8,[4]),1)
        with self.assertRaises(ValueError):label_window(4,4,[])

if __name__=="__main__":unittest.main()
