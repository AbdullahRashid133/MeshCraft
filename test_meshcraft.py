# test_meshcraft.py
"""
Tests for MeshCraft module.
"""

import unittest
from meshcraft import MeshCraft

class TestMeshCraft(unittest.TestCase):
    """Test cases for MeshCraft class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MeshCraft()
        self.assertIsInstance(instance, MeshCraft)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MeshCraft()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
