function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    let res = [];

    nums1.forEach((num) => {
        let itr = 0;
        for (let i=0; i<nums2.length; i++) {
            if (num == nums2[i]) itr = i;
        }

        let next = -1;
        for (let i=itr+1; i<nums2.length; i++) {
            if (nums2[i] > nums2[itr]) {
                next = nums2[i];
                res.push(next);
                break;
            }
        }

        if (next == -1) res.push(next);
    });

    return res;
};