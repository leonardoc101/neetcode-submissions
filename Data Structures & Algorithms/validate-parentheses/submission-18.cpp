class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> pairs = {
            {'}', '{'},
            {']', '['},
            {')', '('},
        };

        std::vector<char> stack;
        for (char c : s){
            if (pairs.count(c)) {
                if (stack.empty() || stack.back() != pairs[c]) {
                    return false;
                } else {
                    stack.pop_back();
                }
            } else {
                stack.push_back(c);
            }
        }
        return stack.empty();
    }
};
