import pandas as pd
import glob
import os

def process_results():
    results = []
    sizes = [8, 50, 100, 1000, 10000, 50000, 100000]
    
    for size in sizes:
        try:
            # Read sequential output
            with open(f"sequential_output{size}.txt", 'r') as f:
                seq_length = int(f.readline().strip())
                seq_lcs = f.readline().strip()
                seq_time = float(f.readline().strip())
            
            # Read parallel output
            with open(f"parallel_output{size}.txt", 'r') as f:
                par_length = int(f.readline().strip())
                par_lcs = f.readline().strip()
                par_time = float(f.readline().strip())
            
            # Calculate speedup
            speedup = seq_time / par_time if par_time > 0 else float('nan')
            
            results.append({
                'Input Size': size,
                'String Length': seq_length,
                'Sequential String': seq_lcs,
                'Parallel String': par_lcs,
                'Sequential Time (s)': seq_time,
                'Parallel Time (s)': par_time,
                'Speedup': speedup
            })
            
        except Exception as e:
            print(f"Error processing size {size}: {str(e)}")
            results.append({
                'Input Size': size,
                'String Length': float('nan'),
                'Sequential String': 'N/A',
                'Parallel String': 'N/A',
                'Sequential Time (s)': float('nan'),
                'Parallel Time (s)': float('nan'),
                'Speedup': float('nan')
            })
    
    # Create DataFrame and save to Excel
    df = pd.DataFrame(results)
    df.to_excel('lcs_results.xlsx', index=False)
    print("Results have been saved to lcs_results.xlsx")

if __name__ == "__main__":
    process_results()