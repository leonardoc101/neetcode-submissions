class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::set<int> numSet(nums.begin(), nums.end());
        int longest = 0;
        
        for (int num : numSet) {
            if (!(numSet.contains(num - 1))) {
                int length = 1;
                while (numSet.contains(num + length)) {
                    length++;
                }
                longest = std::max(longest, length);
            }
        }
        return longest;
    }
};
