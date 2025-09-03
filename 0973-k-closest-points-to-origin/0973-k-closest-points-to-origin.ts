function kClosest(points: number[][], k: number): number[][] {
    let maxHeap = new MaxPriorityQueue<number[]>(
        (p) => euclidDist(p),
    );

    for (let p of points) {
        maxHeap.enqueue(p);
        if (maxHeap.size() > k) {
            maxHeap.dequeue();
        }
    }

    return maxHeap.toArray();
};

function euclidDist(point: number[]): number {
    return point[0]**2 + point[1]**2;
}