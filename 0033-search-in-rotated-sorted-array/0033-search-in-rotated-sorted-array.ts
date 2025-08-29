function search(nums: number[], target: number): number {
    let n = nums.length-1;
    let start = 0;
    let end = n;

    while (start <= end) {
        let mid = start + Math.floor((end-start)/2);

        if (nums[mid] === target) {
            return mid;
        } else if (nums[start] <= nums[mid]) {
            if (nums[start] <= target && target < nums[mid])
                end = mid-1;
            else start = mid+1;
        } else {
            if (nums[mid] < target && target <= nums[end]) 
                start = mid+1;
            else end = mid-1;
        }
    }

    return -1;
};