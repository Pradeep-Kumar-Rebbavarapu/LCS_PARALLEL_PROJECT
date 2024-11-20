import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Define the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Colors for plotting
colors = {
    'Sequential': 'red',
    'Anti-Diagonal': 'blue',
    'Divide-and-Conquer': '#2ca02c'
}

# Load Data
data_path = os.path.join(BASE_DIR, '../../databases/sequential_vs_anti_diagonal/results.csv')
df = pd.read_csv(data_path)

# Sanitize Data: Ensure all values are finite
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# Define the x-tick values for the bar plot
x_ticks = [5, 10, 100, 200, 500, 1000, 10000]

# --- Bar Graph (Sequential vs Anti-Diagonal) ---
fig, ax = plt.subplots(figsize=(10, 6))

# Bar Plot: Sequential vs Anti-Diagonal
x = np.arange(len(df['Input Size']))
width = 0.35
ax.bar(x - width / 2, df['Sequential Time (s)'], width, label='Sequential', color=colors['Sequential'])
ax.bar(x + width / 2, df['Anti-Diagonal Time (s)'], width, label='Anti-Diagonal', color=colors['Anti-Diagonal'])

# Bar Plot Settings for x-ticks
ax.set_xticks(np.arange(len(x_ticks)))  # Ensure the number of ticks corresponds to the given list
ax.set_xticklabels(x_ticks, rotation=45, fontsize=12)  # Set custom tick labels
ax.set_xlabel('Input Size', fontsize=14)
ax.set_ylabel('Time (s)', fontsize=14)
ax.set_title('Time Taken: Sequential vs Anti-Diagonal (Bar Graph)', fontsize=16)
ax.legend(fontsize=12)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Annotate Bars
for i in range(len(x_ticks)):
    ax.text(i - width / 2, df['Sequential Time (s)'][i] + 0.1, f"{df['Sequential Time (s)'][i]:.2f}", ha='center', fontsize=10)
    ax.text(i + width / 2, df['Anti-Diagonal Time (s)'][i] + 0.1, f"{df['Anti-Diagonal Time (s)'][i]:.2f}", ha='center', fontsize=10)

# Save Bar Graph
bar_output_image_path = os.path.join(BASE_DIR, '../../images/sequential_vs_anti_diagonal_bar.png')
plt.tight_layout()
plt.savefig(bar_output_image_path)
plt.close()

# --- Line Graph (Speedup) ---
fig, ax = plt.subplots(figsize=(10, 6))

# Line Plot: Speedup for Anti-Diagonal
ax.plot(df['Input Size'], df['Speedup'], label='Anti-Diagonal', color=colors['Anti-Diagonal'], marker='s', markersize=8, linewidth=2)

# Line Plot Settings
ax.set_xlabel('Input Size', fontsize=14)
ax.set_ylabel('Speedup', fontsize=14)
ax.set_title('Speedup for Anti-Diagonal (Line Plot)', fontsize=16)
ax.legend(fontsize=12)
ax.grid(linestyle='--', alpha=0.7)

# Save Speedup Graph
speedup_output_image_path = os.path.join(BASE_DIR, '../../images/sequential_vs_anti_diagonal_speedup.png')
plt.tight_layout()
plt.savefig(speedup_output_image_path)
plt.close()

