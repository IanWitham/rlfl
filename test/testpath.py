import unittest

import sys
sys.path.append('..')

import rlfl
from tmap import MAP as m
TMAP, TORIGOS = m
from emap import MAP as m
EMAP, EORIGOS = m

class TestPath(unittest.TestCase):  
    def setUp(self):
        self.map = rlfl.create_map(len(TMAP), len(TMAP[0]))
        for row in range(len(TMAP)):
            for col in range(len(TMAP[row])):
                if TMAP[row][col] != '#':
                    rlfl.set_flag(self.map, row, col, rlfl.CELL_SEEN) 
                    rlfl.set_flag(self.map, row, col, rlfl.CELL_OPEN) 
    
    def test_path_astar(self):
        p, p1, p2, p3, p4, p5, p6, p7, p8, p9 = TORIGOS
        path = rlfl.path(self.map, p, p3, rlfl.PATH_ASTAR, -1, 0, 10.0)
        self.assertEqual(len(path), 16)
        diagonal_path = rlfl.path(self.map, p, p3, rlfl.PATH_ASTAR, -1, 0, 0.0)
        self.assertEqual(len(path), 16)
        self.assertEqual(path, diagonal_path)
        path = rlfl.path(self.map, p1, p3, rlfl.PATH_ASTAR, -1, 0, 10.0)
        self.assertFalse(path)
        path = rlfl.path(self.map, p1, p2, rlfl.PATH_ASTAR, -1, 0, 10.0)
        self.assertEqual(len(path), 6)
        diagonal_path = rlfl.path(self.map, p1, p2, rlfl.PATH_ASTAR, -1, 0, 0.0)
        self.assertEqual(diagonal_path, ((15, 11), (15, 10), (14, 9), 
                                         (15, 8), (14, 7), (15, 6)))
        self.assertNotEqual(path, diagonal_path)
        
#        self.print_path(path, p1, p3, TMAP)
        
    def test_path_basic(self):
        p, p1, p2, p3, p4, p5, p6, p7, p8, p9 = TORIGOS
        path = rlfl.path(self.map, p, p3)
#        self.assertEqual(len(path), 2)
        self.print_path(path, p, p3, TMAP)
        
        path = rlfl.path(self.map, p, p3, rlfl.PATH_BASIC, -1, rlfl.PROJECT_THRU)
#        self.assertEqual(len(path), 1)
        self.print_path(path, p, p3, TMAP)
    
    def print_path(self, path, S, T, using):
        if not path:
            print('NO PATH')
            return
        print('\n->')
        for row in range(len(using)):
            for col in range(len(using[row])):
                if (row, col) == T:
                    print('T', end="")
                elif (row, col) == S:
                    print('S', end="")
                elif (row, col) in path:
                    print('*', end="")
                else:
                    print(using[row][col], end="")
            print()
        print('<-')

if __name__ == '__main__':
    unittest.main()