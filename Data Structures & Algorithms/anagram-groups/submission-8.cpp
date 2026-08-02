class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string> strs) {
        std::vector<vector<string>> out;
        while (strs.size() != 0) {
            std::string word = strs.back();
            strs.pop_back();
            std::vector<string> sub_out = {word};
            int i = 0;
            while (i < strs.size()){ 
                if (isAnagram(word, strs[i])) {
                    sub_out.push_back(strs[i]);
                    strs.erase(strs.begin() + i);
                } else {
                    i++;
                }
            }
            out.push_back(sub_out);
        }
        return out;
    }

    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false; 
        }
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        return s == t;
    }
};
