# test_hingerift.py
"""
Tests for HingeRift module.
"""

import unittest
from hingerift import HingeRift

class TestHingeRift(unittest.TestCase):
    """Test cases for HingeRift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HingeRift()
        self.assertIsInstance(instance, HingeRift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HingeRift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
