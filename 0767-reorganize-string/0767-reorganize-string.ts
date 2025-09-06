function reorganizeString(s: string): string {
    let maxHeap = new MaxPriorityQueue<[string, number]>(
        (p) => p[1]
    );
    let map = new Map<string, number>();

    for (const ch of s)
        map.set(ch, (map.get(ch) ?? 0) + 1);

    for (const [key, val] of map.entries())
        maxHeap.enqueue([key, val]); 

    let res = "";
    while (maxHeap.size() > 1) {
        let [pa1, pb1] = maxHeap.dequeue();
        let [pa2, pb2] = maxHeap.dequeue();

        res += pa1 + pa2;
        
        if (--pb1 > 0) maxHeap.enqueue([pa1, pb1]);
        if (--pb2 > 0) maxHeap.enqueue([pa2, pb2]);
    }

    if (maxHeap.size() > 0) {
        let [p, f] = maxHeap.dequeue();
        if (f > 1) return "";
        res += p;
    }

    return res;
};