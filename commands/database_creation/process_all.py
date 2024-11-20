import pandas as pd
import os

# Define the base directory (current script location)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

results = []
sizes = [5,10,100,200,500,1000,10000]

for size in sizes:
    try:
        # Paths to the output files
        sequential_path = os.path.join(BASE_DIR, f"../../outputs/sequential/output{size}.txt")
        anti_diagonal_path = os.path.join(BASE_DIR, f"../../outputs/anti_diagonal/output{size}.txt")
        divide_and_conquer_path = os.path.join(BASE_DIR, f"../../outputs/divide_and_conquer/output{size}.txt")
        
        # Read sequential output
        with open(sequential_path, 'r') as f:
            seq_length = int(f.readline().strip())
            seq_lcs = f.readline().strip()
            seq_time = float(f.readline().strip())
        
        # Read anti-diagonal output
        with open(anti_diagonal_path, 'r') as f:
            ad_length = int(f.readline().strip())
            ad_lcs = f.readline().strip()
            ad_time = float(f.readline().strip())
        
        # Read divide-and-conquer output
        with open(divide_and_conquer_path, 'r') as f:
            dc_length = int(f.readline().strip())
            dc_lcs = f.readline().strip()
            dc_time = float(f.readline().strip())
        
        # Calculate speedups
        ad_speedup = seq_time / ad_time if ad_time > 0 else float('nan')
        dc_speedup = seq_time / dc_time if dc_time > 0 else float('nan')
        
        results.append({
            'Input Size': size,
            'String Length': seq_length,
            'Sequential String': seq_lcs,
            'Anti-Diagonal String': ad_lcs,
            'Divide-and-Conquer String': dc_lcs,
            'Sequential Time (s)': seq_time,
            'Anti-Diagonal Time (s)': ad_time,
            'Divide-and-Conquer Time (s)': dc_time,
            'Anti-Diagonal Speedup': ad_speedup,
            'Divide-and-Conquer Speedup': dc_speedup
        })
        
    except Exception as e:
        print(f"Error processing size {size}: {str(e)}")
        results.append({
            'Input Size': size,
            'String Length': float('nan'),
            'Sequential String': 'N/A',
            'Anti-Diagonal String': 'N/A',
            'Divide-and-Conquer String': 'N/A',
            'Sequential Time (s)': float('nan'),
            'Anti-Diagonal Time (s)': float('nan'),
            'Divide-and-Conquer Time (s)': float('nan'),
            'Anti-Diagonal Speedup': float('nan'),
            'Divide-and-Conquer Speedup': float('nan')
        })

# Create DataFrame and save to database
database_path = os.path.join(BASE_DIR, "../../databases/all/results.csv")
df = pd.DataFrame(results)
df.to_csv(database_path, index=False)
print(f"Results have been saved to '{database_path}'.")
