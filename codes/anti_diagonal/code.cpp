#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>
#include <omp.h>

using namespace std;
using namespace std::chrono;

class AntiDiagonalLCS {
private:
    string s1, s2;
    int m, n;

public:
    AntiDiagonalLCS(const string& str1, const string& str2)
        : s1(str1), s2(str2), m(str1.length()), n(str2.length()) {}

    pair<int, string> computeLCS() {
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int diagonal = 1; diagonal <= m + n; ++diagonal) {
            #pragma omp parallel for
            for (int j = max(0, diagonal - m); j <= min(diagonal, n); ++j) {
                int i = diagonal - j;

                if (i > 0 && j > 0) {
                    if (s1[i - 1] == s2[j - 1]) {
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
            if (s1[i - 1] == s2[j - 1]) {
                lcs = s1[i - 1] + lcs;
                i--;
                j--;
            } else if (dp[i - 1][j] > dp[i][j - 1]) {
                i--;
            } else {
                j--;
            }
        }

        return {dp[m][n], lcs};
    }
};

void process_input(int size) {
    string input_file = "../../inputs/input" + to_string(size) + ".txt";
    string output_file = "../../outputs/anti_diagonal/output" + to_string(size) + ".txt";

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
    AntiDiagonalLCS solver(S1, S2);
    auto [length, lcs] = solver.computeLCS();
    auto end = high_resolution_clock::now();
    duration<double> time_taken = end - start;
    cout<<length<<endl;
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
    vector<int> sizes = {5, 10, 100, 200, 500, 1000, 10000};
    
    for (int size : sizes) {
        process_input(size);
    }
    
    return 0;
}
