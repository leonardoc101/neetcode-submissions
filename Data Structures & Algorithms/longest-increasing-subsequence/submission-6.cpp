class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> dp;
        dp = std::vector<int>(n, 1);

        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] < nums[j]) {
                    dp[i] = std::max(dp[i], 1 + dp[j]);
                }
            }
        }
        return std::ranges::max(dp);
    }
};
