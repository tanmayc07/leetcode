function frequencySort(s: string): string {
    let maxHeap = new MaxPriorityQueue<[string, number]>(
        (p) => p[1]
    );

    let map = new Map<string, number>();
    for (const c of s)
        map.set(c, (map.get(c) ?? 0) + 1);

    for (const [c, freq] of map.entries()) 
        maxHeap.enqueue([c, freq]);

    let res = "";
    while (maxHeap.size() > 0) {
        const [ch, freq] = maxHeap.dequeue();
        res += ch.repeat(freq);
    }

    return res;
};