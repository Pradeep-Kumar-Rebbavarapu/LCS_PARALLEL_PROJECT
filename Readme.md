# Parallel vs Sequential LCS Benchmark

This project compares the performance of parallel and sequential algorithms for calculating the Longest Common Subsequence (LCS).

## Getting Started

The repository contains the following files:

- `commands/generate_input.py`: Python script to generate random input data (two sequences).
- `codes/sequential/code.cpp`: C++ implementation for sequential LCS calculation.
- `codes/anti_diagonal/code.cpp`: C++ implementation for parallel (anti-diagonal) LCS calculation.
- `generate_database_and_graph.sh`: Bash script to Convert output.txt to excel sheets and generate performance graphs.

## Prerequisites

- C++ compiler
- Python 3
- OpenMP (for the parallel implementation)
- Matplotlib, Pandas, NumPy (for generating graphs)

## Running the Code

1. **Generate Input Data**:

    ```bash
    python3 commands/generate_input.py
    ```

    This will create an `input.txt` file containing two randomly generated sequences.

2. **Run the Sequential LCS Algorithm**:

    ```bash
    g++ codes/sequential/code.cpp -o codes/sequential/sequential
    codes/sequential/sequential
    ```

    This will produce an `output.txt` file containing the LCS length and the sequence (if applicable).

3. **Run the Parallel (Anti-Diagonal) LCS Algorithm**:

    ```bash
    g++ codes/anti_diagonal/code.cpp -fopenmp -o codes/anti_diagonal/anti_diagonal
    codes/anti_diagonal/anti_diagonal
    ```

    This will also produce an `output.txt` file with the LCS length and sequence (if applicable).

4. **Generate the Database and Graphs**:

    ```bash
    ./generate_database_and_graph.sh
    ```

    This script will create a CSV file in the `databases` folder for performance data and generate graphs in the `images` folder for comparison.

## Contributing

If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
