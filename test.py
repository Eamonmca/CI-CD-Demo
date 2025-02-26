import unittest

def gc_content(seq: str) -> float:
    """Calculate the GC content percentage of a DNA sequence."""
    seq = seq.upper()
    if not seq:
        return 0.0
    gc_count = seq.count('G') + seq.count('C')
    return (gc_count / len(seq)) * 100

class TestGenomicsFunctions(unittest.TestCase):
    def test_gc_content_all_gc(self):
        self.assertEqual(gc_content("GCGCGC"), 100.0)

    def test_gc_content_no_gc(self):
        self.assertEqual(gc_content("ATATAT"), 0.0)

    def test_gc_content_mixed(self):
        # 'ATGC' has 50% GC content.
        self.assertAlmostEqual(gc_content("ATGC"), 50.0)
        
    def test_gc_content_empty(self):
        self.assertEqual(gc_content(""), 0.0)

if __name__ == '__main__':
    unittest.main()
