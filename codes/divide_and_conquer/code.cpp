#include <iostream>
#include <vector>
#include <omp.h>

using namespace std;

// Function to compute the cost matrix for LCS
void computeCostMatrix(const vector<char>& A, const vector<char>& B, vector<vector<int>>& DG) {
    int m = A.size();
    int n = B.size();

    #pragma omp parallel for
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (A[i - 1] == B[j - 1]) {
                DG[i][j] = DG[i - 1][j - 1] + 1;
            } else {
                DG[i][j] = max(DG[i - 1][j], DG[i][j - 1]);
            }
        }
    }
}

// Function to trace the LCS path from the DP matrix
void traceLCSPath(const vector<vector<int>>& DG, vector<char>& LCS, const vector<char>& A, int m, int n) {
    int i = m, j = n;
    int index = 0;

    // Tracing the path backward from (m, n) to (1, 1)
    while (i > 0 && j > 0) {
        if (DG[i][j] == DG[i - 1][j - 1] + 1) {
            LCS[index++] = A[i - 1]; // Match found
            i--;
            j--;
        } else if (DG[i][j] == DG[i - 1][j]) {
            i--;
        } else {
            j--;
        }
    }

    // Reverse LCS as we traced it backward
    reverse(LCS.begin(), LCS.end());
}

// Main function to compute the LCS using OpenMP
vector<char> LCS_OpenMP(const vector<char>& A, const vector<char>& B) {
    int m = A.size();
    int n = B.size();
    vector<vector<int>> DG(m + 1, vector<int>(n + 1, 0));

    // Compute the cost matrix using OpenMP
    computeCostMatrix(A, B, DG);

    // Trace the LCS from the DP matrix
    vector<char> LCS(DG[m][n]);
    traceLCSPath(DG, LCS, A, m, n);

    return LCS;
}

int main() {
    string A = "qvciw";
    string B = "qmydc";

    // Convert strings to vectors of characters
    vector<char> A_vec(A.begin(), A.end());
    vector<char> B_vec(B.begin(), B.end());

    // Compute LCS using the OpenMP approach
    vector<char> lcs = LCS_OpenMP(A_vec, B_vec);

    // Output the result
    cout << "Longest Common Subsequence: ";
    for (char c : lcs) {
        cout << c;
    }
    cout << endl;

    return 0;
}
