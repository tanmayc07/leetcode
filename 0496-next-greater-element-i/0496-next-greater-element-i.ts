function nextGreaterElement(nums1: number[], nums2: number[]): number[] {
    let res = [];
    let mp = new Map<number, number>();
    let st = [];

    for (let i=nums2.length-1; i>=0; i--) {
        while (st.length>0 && st[st.length-1] <= nums2[i])
            st.pop();
        
        if (st.length == 0) mp[nums2[i]] = -1;
        else mp[nums2[i]] = st[st.length-1];

        st.push(nums2[i]);
    }

    for (let i=0; i<nums1.length; i++) 
        res.push(mp[nums1[i]]);

    return res;
};