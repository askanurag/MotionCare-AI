import unittest,tempfile
from pathlib import Path
import numpy as np

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x=np.random.default_rng(42).normal(size=(600,6))

    def test_behavior(self):
        from healthcare_ai.stream_buffer import WindowBuffer
        from healthcare_ai.windowing import windows
        buffer=WindowBuffer();out=[]
        for chunk in np.array_split(self.x,7):out.extend(buffer.push(chunk))
        expected=windows(self.x,50)
        self.assertEqual(len(out),len(expected))
        for a,(_,_,b) in zip(out,expected):np.testing.assert_array_equal(a,b)

if __name__=="__main__":unittest.main()
