#include <iostream>
#include <string>
#include <vector>
 
bool is_isogram(std::string string) {
    std::string lower_string;
    for (char c : string) {
        lower_string += std::tolower(c);
    }
    std::vector<char> chars;
    for (char i : lower_string) {
        if (std::find(chars.begin(), chars.end(), i) != chars.end()) {
            return false;
        }
        chars.push_back(i);
    }
    return true;
}
