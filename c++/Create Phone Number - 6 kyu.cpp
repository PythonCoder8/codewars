#include <string>
using namespace std;

std::string createPhoneNumber(const int arr [10]){
  string number = "";
  for (int i = 0; i < 10; i++)
    number += to_string(arr[i]);
    
  number.insert(0, "(");
  number.insert(4, ") ");
  number.insert(9, "-");
  
  return number;
}
