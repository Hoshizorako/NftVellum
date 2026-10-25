# test_nftvellum.py
"""
Tests for NftVellum module.
"""

import unittest
from nftvellum import NftVellum

class TestNftVellum(unittest.TestCase):
    """Test cases for NftVellum class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = NftVellum()
        self.assertIsInstance(instance, NftVellum)

    def test_run_method(self):
        """Test the run method."""
        instance = NftVellum()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
