class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mmap = {'U':[0, 1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}
        start = [0,0]

        for i in range(len(moves)):
            start[0] += mmap[moves[i]][0]
            start[1] += mmap[moves[i]][1]
        
        return start == [0,0]