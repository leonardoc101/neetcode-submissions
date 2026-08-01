class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> count;
        for (int num : nums) {
            auto two = count.find(num);
            if (two != count.end()) {
                count[num] = 1 + two->second;
            } else {
                count[num] = 1;
            }
        }
        std::vector<std::pair<int, int>> arr;
        for (const auto& [num, freq] : count) {
            arr.push_back({freq, num});
        }
        std::sort(arr.begin(), arr.end());

        std::vector<int> res;
        while (res.size() < k) {
            res.push_back(arr.back().second);
            arr.pop_back();
        }
        return res;
    }
};
