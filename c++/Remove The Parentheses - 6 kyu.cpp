#include <string>

std::string remove_parentheses(const std::string &str)
{
  int o = 0;
  std::string s;
  for (const char& c: str) 
    if (c == '(') o++ ;
      else if (c == ')') o--; 
        else if (!o) s = s + c;
  return s;
}
