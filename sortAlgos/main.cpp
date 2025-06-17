#include "sortHeader.h"
#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

void printVector(const vector<int>& v) {
  for (int num : v) {
      cout << num << " ";
  }
  cout << endl;
}

int main() {
  vector<int> v = {2, 5, 3, 4, 6};

  /*
  INSERTION SORT
  cout << "Before sorting: ";
  printVector(v);

  insertionSort(v);

  cout << "After sorting: ";
  printVector(v);

  insertionSortReverse(v);

  cout << "After sorting Reverse: ";
  printVector(v);

  */

  
  int num = searchVector(v, 3);
  cout << num << endl;
  return 0;
}
