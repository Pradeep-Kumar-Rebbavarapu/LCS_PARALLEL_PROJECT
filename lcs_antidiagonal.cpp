// lcs_antidiagonal.cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>
#include <omp.h>

using namespace std;
using namespace chrono;


pair<int, string> lcsAntiDiagonal(const string& S1, const string& S2) {
    int m = S1.length(), n = S2.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));


    for (int k = 1; k <= m + n - 1; k++) {
        int j_start = max(0, k - m);
        int j_end = min(k, n);

        #pragma omp parallel for
        for (int j = j_start; j <= j_end; j++) {
            int i = k - j;
            if (i > 0 && i <= m && j > 0 && j <= n) {
                if (S1[i - 1] == S2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
    }


    string lcs;
    int i = m, j = n;
    while (i > 0 && j > 0) {
        if (S1[i - 1] == S2[j - 1]) {
            lcs = S1[i - 1] + lcs;
            i--, j--;
        } else if (dp[i - 1][j] > dp[i][j - 1]) {
            i--;
        } else {
            j--;
        }
    }

    return {dp[m][n], lcs};
}

void process_input(int size) {
    string input_file = "input" + to_string(size) + ".txt";
    string output_file = "parallel_output" + to_string(size) + ".txt";

    // Read input
    ifstream input(input_file);
    if (!input) {
        cerr << "Could not open input file: " << input_file << endl;
        return;
    }

    int m, n;
    input >> m >> n;
    string S1, S2;
    input >> S1 >> S2;
    input.close();


    auto start = high_resolution_clock::now();
    auto [length, lcs] = lcsAntiDiagonal(S1, S2);
    auto end = high_resolution_clock::now();
    duration<double> time_taken = end - start;


    ofstream output(output_file);
    if (!output) {
        cerr << "Could not open output file: " << output_file << endl;
        return;
    }

    output << length << endl;
    output << lcs << endl;
    output << time_taken.count() << endl;
    output.close();

    cout << "Processed size " << size << ": Time = " << time_taken.count() << "s" << endl;
}

int main() {
    vector<int> sizes = {8, 50, 100, 1000, 10000};
    
    for (int size : sizes) {
        process_input(size);
    }
    
    return 0;
}