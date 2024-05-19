#include <iostream>
#include <vector>

using namespace std;

void inputMatrix(vector<vector<int>>& matrix, int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        vector<int> row(cols);
        for (int j = 0; j < cols; ++j) {
            cin >> row[j];
        }
        matrix.push_back(row);
    }
}

void printMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
}

vector<vector<int>> multiplyMatrices(const vector<vector<int>>& A, const vector<vector<int>>& B, int m, int n, int p) {
    vector<vector<int>> result(m, vector<int>(p, 0));

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < p; ++j) {
            for (int k = 0; k < n; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return result;
}

int main() {
    int m, n, p;
    cout << "Enter the number of rows and columns of matrix A (m and n): ";
    cin >> m >> n;
    cout << "Enter the number of columns of matrix B (p): ";
    cin >> p;

    vector<vector<int>> A;
    vector<vector<int>> B;

    cout << "Enter the elements of matrix A:" << endl;
    inputMatrix(A, m, n);

    cout << "Enter the elements of matrix B:" << endl;
    inputMatrix(B, n, p);

    vector<vector<int>> result = multiplyMatrices(A, B, m, n, p);

    cout << "Resulting matrix after multiplication:" << endl;
    printMatrix(result);

    return 0;
}
