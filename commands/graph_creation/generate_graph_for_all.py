import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Define the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the path for the CSV file
csv_file_path = os.path.join(BASE_DIR, '../../databases/all/results.csv')

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Plot Time Taken for Sequential and Parallel
plt.figure(figsize=(20, 10))
x = np.arange(len(df['Input Size']))
width = 0.25
plt.bar(x - width, df['Sequential Time (s)'], width, label='Sequential')
plt.bar(x, df['Anti-Diagonal Time (s)'], width, label='Anti-Diagonal')
plt.bar(x + width, df['Divide-and-Conquer Time (s)'], width, label='Divide-and-Conquer')

# Format x-axis labels as powers of 10 for both plots
plt.xticks(x, [f"$10^{int(i)}$" for i in df['Input Size']])

plt.xlabel('Input Size')
plt.ylabel('Time (s)')
plt.title('Time Taken for Sequential and Parallel')
plt.legend()

# Save the plot
time_taken_path = os.path.join(BASE_DIR, '../../images/time_taken.png')
plt.savefig(time_taken_path)
plt.close()

# Plot Speedup with blue color and blue dots
plt.figure(figsize=(20, 10))
plt.plot(df['Input Size'], df['Anti-Diagonal Speedup'], label='Anti-Diagonal Speedup', color='blue', marker='o', markersize=8, linestyle='-', linewidth=2)
plt.plot(df['Input Size'], df['Divide-and-Conquer Speedup'], label='Divide-and-Conquer Speedup', color='blue', marker='o', markersize=8, linestyle='-', linewidth=2)

# Format x-axis labels as powers of 10 for the speedup plot
plt.xticks(df['Input Size'], [f"$10^{int(i)}$" for i in df['Input Size']])

# Set y-axis to be in scientific notation
plt.gca().yaxis.set_major_formatter(ScalarFormatter('e'))

# Adjust y-axis to show values like 10^-4, 10^-3, ...
plt.ticklabel_format(axis='y', style='sci', scilimits=(-4, -3))

plt.xlabel('Input Size')
plt.ylabel('Speedup')
plt.title('Speedup')
plt.legend()

# Save the plot
speedup_path = os.path.join(BASE_DIR, '../../images/speedup.png')
plt.savefig(speedup_path)
plt.close()

print(f"Graphs have been saved to {BASE_DIR}/images")
