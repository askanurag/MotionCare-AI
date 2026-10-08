import unittest,tempfile
from pathlib import Path
import numpy as np
from healthcare_ai.domain_simulation import make_recording

class TestCase(unittest.TestCase):
    def setUp(self):
        self.record=make_recording(7)

    def test_behavior(self):
        import matplotlib;matplotlib.use('Agg')
        from healthcare_ai.domain_visualization import plot_recording
        import matplotlib.pyplot as plt
        fig=plot_recording(self.record);self.assertEqual(len(fig.axes),1);plt.close(fig)

if __name__=="__main__":unittest.main()
