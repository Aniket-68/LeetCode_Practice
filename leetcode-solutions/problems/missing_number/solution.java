class Solution {
    public int missingNumber(int[] nums) {
        int actual_sum=0,sum=0,n=nums.length;

        actual_sum=n*(n+1)/2;

        for(int i=0;i<n;i++)
        {
            sum+=nums[i];
        }

        return (actual_sum-sum);


    }
}