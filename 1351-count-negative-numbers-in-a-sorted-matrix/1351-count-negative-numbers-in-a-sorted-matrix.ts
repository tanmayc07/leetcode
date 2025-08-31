function countNegatives(grid: number[][]): number {
    let rows = grid.length;
    let cols = grid[0].length;
    let res = 0;

    for(let r = rows-1, c = 0; r >= 0 && c < cols;) {
        if (grid[r][c] < 0) {
            res += cols-c;
            r--;
        } else c++; 
    }

    return res;
};