#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

using namespace std;
using namespace chrono;


pair<int, string> lcsSequential(const string& S1, const string& S2) {
    int m = S1.length(), n = S2.length();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

 
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (S1[i - 1] == S2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
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
    string output_file = "sequential_output" + to_string(size) + ".txt";


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
    auto [length, lcs] = lcsSequential(S1, S2);
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