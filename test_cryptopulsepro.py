# test_cryptopulsepro.py
"""
Tests for CryptoPulsePro module.
"""

import unittest
from cryptopulsepro import CryptoPulsePro

class TestCryptoPulsePro(unittest.TestCase):
    """Test cases for CryptoPulsePro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoPulsePro()
        self.assertIsInstance(instance, CryptoPulsePro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoPulsePro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
