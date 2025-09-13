/**
 * Definition for _Node.
 * class _Node {
 *     val: number
 *     next: _Node | null
 *     random: _Node | null
 * 
 *     constructor(val?: number, next?: _Node, random?: _Node) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *         this.random = (random===undefined ? null : random)
 *     }
 * }
 */


function copyRandomList(head: _Node | null): _Node | null {
    let map = new Map<_Node, _Node>();
    map.set(null, null);

    let start = head;
    while (start) {
        map.set(start, new _Node(start.val));
        start = start.next;
    }

    start = head;
    while (start) {
        let copy = map.get(start);
        copy.next = map.get(start.next);
        copy.random = map.get(start.random);
        start = start.next;
    }

    return map.get(head);
};