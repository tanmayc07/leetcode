impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut i = 0;
        let mut j = numbers.len()-1;

        while i < j {
            if numbers[i]+numbers[j] < target {
                i+=1;
            } else if numbers[i]+numbers[j] > target {
                j-=1;
            } else {
                return Vec::from([i as i32 +1, j as i32 +1]);
            }
        }

        return Vec::new();
    }
}