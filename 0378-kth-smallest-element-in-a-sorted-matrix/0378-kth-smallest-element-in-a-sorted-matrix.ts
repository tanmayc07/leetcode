function kthSmallest(matrix: number[][], k: number): number {
    let maxHeap = new MaxPriorityQueue<number>();

    for (let row=0; row<matrix.length; row++) {
        for (let col=0; col<matrix[row].length; col++) {
            maxHeap.enqueue(matrix[row][col]);
            if (maxHeap.size() > k)
                maxHeap.dequeue();
        }
    }

    return maxHeap.dequeue();
};