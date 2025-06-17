#include "sortHeader.h"
// include for printing cout, endl
#include <iostream>
// include for vector
#include <vector>

// used to remove the std:: notation before each reference
using std::cout;
using std::endl;
using std::vector;

// pass the variable by reference to modify vector
void insertionSort(vector<int>& v) {
  int n = v.size();

  // v points to the entire vector object

  if (n < 2) {
      return;
  }

  // assume every part before is sorted
  // input: unsorted list
  // output: sorted list
  // pick elem A[i]
  // move elem A[i] to the left while A[i] < A[j] or i > 0
  // move A[j] -> A[j+1] as we need to shift everything over
  // once found A[i] > A[j] insert to the right

  for (int i = 1; i < n; i++) {
    int curr = v[i];
    int j = i - 1;

    while (j > -1 && curr < v[j]) {
      v[j+1] = v[j];
      j--;
    }

    v[j+1] = curr;
  }
}

void insertionSortReverse(vector<int>& v) {
  int n = v.size();

  // v points to the entire vector object

  if (n < 2) {
      return;
  }

  // assume every part before is sorted
  // input: unsorted list
  // output: sorted list
  // pick elem A[i] (curr)
  // move curr to the left while (j > -1 && A[j] < curr)
  // move A[j] - > A[j + 1]
  // set A[j + 1] == curr

  for (int i = 1; i < n; i++) {
    int curr = v[i];
    int j = i - 1;

    while (j > -1 && v[j] < curr) {
      v[j + 1] = v[j];
      j--;
    }
    v[j + 1] = curr;
  }
}

int searchVector(std::vector<int>& A, int v) {
  if (A.empty())  return -1 ;
  
  for (int i = 0; i < A.size(); i++) {
    if (A[i] == v) {
      return i;
    }
  }

  return -1;
}