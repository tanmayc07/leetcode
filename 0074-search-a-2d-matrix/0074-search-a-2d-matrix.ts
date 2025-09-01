function searchMatrix(matrix: number[][], target: number): boolean {
    let itr;
    let itr_end = matrix.length;
    

    let fnd = 0;
    for(itr=0; itr<itr_end; itr++) {
        if (!fnd) {
            let start = 0;
            let end = matrix[0].length;

            while (start <= end) {
                let mid = start + Math.floor((end-start)/2);

                if (matrix[itr][mid] == target) {
                    fnd = 1;
                    break;
                } else if (matrix[itr][mid]<target) start = mid+1;
                else end = mid-1;
            }
        }
    }

    return fnd === 1;
};