class Solution {
public:
    bool isAnagram(string s, string t) {
        if (!(s.length() == t.length())) {
            return false; 
        }
        std::vector<char> t_list;
        std::vector<char> s_list;
        for (char p : t){
            t_list.push_back(p);
        }
        for (char c : s){
            s_list.push_back(c);
        }
        std::sort(t_list.begin(), t_list.end());
        std::sort(s_list.begin(), s_list.end());
        if (!(t_list == s_list)){
            return false;
        }
        return true;
    }
};
