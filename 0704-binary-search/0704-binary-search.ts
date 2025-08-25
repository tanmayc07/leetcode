function search(nums: number[], target: number): number {
    let start: number = 0;
    let end: number = nums.length - 1;

    while(start <= end) {
        let mid = start + Math.floor((end-start)/2);

        if(nums[mid] == target)
            return mid;
        else if(nums[mid] > target) 
            end = mid-1;
        else start = mid+1;
    }

    return -1;
};