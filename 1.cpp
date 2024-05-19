#include <iostream>
#include <vector>

using namespace std;

// Function to delete an element from the array
void deleteElement(vector<int>& arr, int position) {
    if (position < 0 || position >= arr.size()) {
        cout << "Invalid position!" << endl;
        return;
    }
    arr.erase(arr.begin() + position);
}

// Function to print the array
void printArray(const vector<int>& arr) {
    for (int elem : arr) {
        cout << elem << " ";
    }
    cout << endl;
}

int main() {
    int n;
    cout << "Enter the number of elements in the array: ";
    cin >> n;

    vector<int> arr(n);
    cout << "Enter the elements of the array:" << endl;
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int position;
    cout << "Enter the position of the element to be deleted: ";
    cin >> position;

    cout << "Original array: ";
    printArray(arr);

    deleteElement(arr, position);

    cout << "Array after deletion: ";
    printArray(arr);

    return 0;
}
