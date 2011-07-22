import unittest

import sys
sys.path.append('..')

import rlfl
from tmap import MAP as m
MAP, ORIGOS = m

class TestLos(unittest.TestCase):
    def setUp(self):
        rlfl.delete_all_maps()
        self.map = rlfl.create_map(len(MAP), len(MAP[0]))
        for row in range(len(MAP)):
            for col in range(len(MAP[row])):
                if MAP[row][col] != '#':
                    p = (row, col)
                    rlfl.set_flag(self.map, p, rlfl.CELL_SEEN) 
                    rlfl.set_flag(self.map, p, rlfl.CELL_OPEN) 
    
    def test_los(self):
        x, y = ORIGOS[1]
        x1, y1 = ORIGOS[2]
        x2, y2 = ORIGOS[3]
        x3, y3 = ORIGOS[4]
        self.assertFalse(rlfl.los(self.map, (x1, y1), (x3, y3)))
        self.assertFalse(rlfl.los(self.map, (x3, y3), (x1, y1)))
        self.assertFalse(rlfl.los(self.map, (x, y), (x3, y3)))
        self.assertFalse(rlfl.los(self.map, (x3, y3), (x, y)))
        self.assertTrue(rlfl.los(self.map, (x1, y1), (x2, y2)))
        self.assertTrue(rlfl.los(self.map, (x2, y2), (x1, y1)))

if __name__ == '__main__':
    unittest.main()