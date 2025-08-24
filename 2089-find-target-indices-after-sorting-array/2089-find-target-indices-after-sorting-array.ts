function targetIndices(nums: number[], target: number): number[] {
    let start: number = 0;
    let end: number = nums.length - 1;
    let res: number[] = [];

    nums.sort((a, b) => a-b)
    console.log(nums)

    while(start <= end) {
        let mid = start + Math.floor((end-start)/2);

        if(nums[mid] == target) {
            let itr = mid-1;
            while(nums[itr] == target) {
                res.push(itr);
                itr--;
            }
            res.push(mid);
            itr = mid+1;
            while(nums[itr] == target) {
                res.push(itr);
                itr++;
            }
            break;
        } else if(nums[mid] > target) 
            end = mid-1;
        else start = mid+1;
    }

    return res.sort((a, b) => a-b);
};