class Solution {
public:
    bool isPalindrome(string s) {
        int leng = s.length();
        std::transform(s.begin(), s.end(), s.begin(), [](unsigned char c) {
            return std::tolower(c);
        });
        std::string new_s;

        for (char c : s) {
            if (std::isalnum(c))
            new_s += std::tolower(c);
        }
        std::string reversed = new_s;
        std::reverse(reversed.begin(), reversed.end());
        return reversed == new_s;
    }
};
