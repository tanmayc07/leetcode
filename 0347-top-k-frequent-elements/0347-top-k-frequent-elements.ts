function topKFrequent(nums: number[], k: number): number[] {
    let hm: Map<number, number> = new Map();
    let pq = new MinPriorityQueue<[number, number]>(
        (n) => n[1]
    );

    for (const num of nums) {
        if (hm.has(num)) hm.set(num, (hm.get(num) ?? 0) + 1);
        else hm.set(num, 1);
    }

    for (const [key, val] of hm) {
        pq.enqueue([key, val]);
        if (pq.size() > k) pq.dequeue();
    }

    return pq.toArray().map(num => num[0]);
};