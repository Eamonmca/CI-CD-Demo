"""Module for calculating GC content and testing genomics functions."""

import unittest

def gc_content(seq: str) -> float:
    """Calculate the GC content percentage of a DNA sequence.
    
    Args:
        seq (str): The DNA sequence.
    
    Returns:
        float: The percentage of nucleotides in the sequence that are either G or C.
    """
    seq = seq.upper()
    if not seq:
        return 0.0
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100

class TestGenomicsFunctions(unittest.TestCase):
    """Test cases for the gc_content function."""

    def test_gc_content_all_gc(self):
        """Test that a sequence of only G and C returns 100%."""
        self.assertEqual(gc_content("GCGCGC"), 100.0)

    def test_gc_content_no_gc(self):
        """Test that a sequence with no G or C returns 0%."""
        self.assertEqual(gc_content("ATATAT"), 0.0)

    def test_gc_content_mixed(self):
        """Test that a mixed sequence returns the correct GC content."""
        self.assertAlmostEqual(gc_content("ATGC"), 50.0)

    def test_gc_content_empty(self):
        """Test that an empty sequence returns 0%."""
        self.assertEqual(gc_content(""), 0.0)

if __name__ == '__main__':
    unittest.main()
