function findPeakElement(nums: number[]): number {
    let n = nums.length;
    if (n == 1) return 0;
    if (nums[0] > nums[1]) return 0;
    if (nums[n-1] > nums[n-2]) return n-1;

    let start = 1;
    let end = nums.length - 2;

    while (start <= end) {
        let mid = start + Math.floor((end-start)/2);

        if (nums[mid] > nums[mid-1] && nums[mid] > nums[mid+1])
            return mid;
        else if (nums[mid] > nums[mid-1]) start = mid + 1;
        else end = mid - 1;
    }

    return -1;
};