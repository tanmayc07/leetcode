function searchRange(nums: number[], target: number): number[] {
    let start = 0;
    let end = nums.length - 1;
    let res = [-1, -1];

    while (start <= end) {
        let mid = start + Math.floor((end-start)/2)

        if (nums[mid] == target) {
            res[0] = mid;
            end = mid - 1;
        } else if (nums[mid] < target) start = mid + 1;
        else end = mid - 1;
    }

    start = 0;
    end = nums.length - 1;

    while (start <= end) {
        let mid = start + Math.floor((end-start)/2)

        if (nums[mid] == target) {
            res[1] = mid;
            start = mid + 1;
        } else if (nums[mid] < target) start = mid + 1;
        else end = mid - 1;
    }

    return res;
};