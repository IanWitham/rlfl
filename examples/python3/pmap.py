_MAP = [
    '######################################################',    
    '..........#.........#################################.',
    '....................########################........+.',
    '..........#...................1######################.',
    '..........#.........#####################.###########.',
    '#.#########.........#####################.############',
    '#.#########.........##########0...........####.....6..',
    '#.##3.....+.........#####################.##########..',
    '#.#############+######2......############.............',
    '#.######.....+.......#.......############.##########..',
    '#.############.......#.......#######################..',
    '#.############......./.......#.......####.............',
    '+.############.......#.......#.......########.######..',
    '#.############.......#.......#.......####.........####',
    '#.####################.......#.......####.........####',
    '#.####.........###############.......####.........####',
    '#.####.........#......4......#.......####.........####',
    '#.####.........#.............#.......####.........#...',
    '+.####.........#.............#.......######.#######...',
    '#.####...............................###.......####...',
    '#.####.........#.............####.######.......####...',
    '...............#.............#................5####...',
    '######.........#.............###########.......#######',
    '######################################################',    
]
_ORIGOS = [None] * 10
for row in range(len(_MAP)):
    for col in range(len(_MAP[0])):
        if _MAP[row][col] in '0123456789':
            _ORIGOS[int(_MAP[row][col])] = (row, col) 
            
MAP = (_MAP, _ORIGOS)