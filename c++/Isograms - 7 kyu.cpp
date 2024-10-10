#include <iostream>
#include <string>

using namespace std;

bool is_isogram(string word) {
  bool seen[26] = {false};
  for (char letter : word) {
    letter = tolower(letter);
    if (seen[letter - 'a']) {
      return false;
    }
    seen[letter - 'a'] = true;
  }
  return true;
}
