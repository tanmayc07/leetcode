/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

var solution = function(isBadVersion: any) {
    return function(n: number): number {
        let start = 1;
        let end = n;
        let res = 0;

        while(start <= end) {
            let mid = start + Math.floor((end-start)/2);
            if(isBadVersion(mid)) {
                res = mid;
                end = mid-1;
            } else {
                start = mid+1;
            }
        }
        
        return res;
    };
};