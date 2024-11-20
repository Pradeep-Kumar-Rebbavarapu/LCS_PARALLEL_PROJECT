import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Define the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Colors for plotting
colors = {
    'Sequential': '#1f77b4',
    'Anti-Diagonal': '#ff7f0e',
    'Divide-and-Conquer': '#2ca02c'
}

# Load Data
data_path = os.path.join(BASE_DIR, '../../databases/sequential_vs_anti_diagonal/results.csv')
df = pd.read_csv(data_path)

# Sanitize Data: Ensure all values are finite
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

# Create Figure
fig, axes = plt.subplots(1, 2, figsize=(22, 10))

# Bar Plot: Sequential vs Anti-Diagonal
x = np.arange(len(df['Input Size']))
width = 0.35
axes[0].bar(x - width / 2, df['Sequential Time (s)'], width, label='Sequential', color=colors['Sequential'])
axes[0].bar(x + width / 2, df['Anti-Diagonal Time (s)'], width, label='Anti-Diagonal', color=colors['Anti-Diagonal'])

# Bar Plot Settings
axes[0].set_xticks(x)
axes[0].set_xticklabels([f"$10^{int(np.log10(i))}$" if i != 0 else "0" for i in df['Input Size']], rotation=45, fontsize=12)  # Format Input Size as powers of 10
axes[0].set_xlabel('Input Size', fontsize=14)
axes[0].set_ylabel('Time (s)', fontsize=14)
axes[0].set_title('Time Taken: Sequential vs Anti-Diagonal (Bar Graph)', fontsize=16)
axes[0].legend(fontsize=12)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Annotate Bars
for i in range(len(df['Input Size'])):
    axes[0].text(i - width / 2, df['Sequential Time (s)'][i] + 0.1, f"{df['Sequential Time (s)'][i]:.2f}", ha='center', fontsize=10)
    axes[0].text(i + width / 2, df['Anti-Diagonal Time (s)'][i] + 0.1, f"{df['Anti-Diagonal Time (s)'][i]:.2f}", ha='center', fontsize=10)


# Plot Speedup in Blue with Blue Dots
axes[1].plot(df['Input Size'], df['Anti-Diagonal Speedup'], label='Anti-Diagonal Speedup', color='blue', marker='o', markersize=8, linestyle='-', linewidth=2)
axes[1].plot(df['Input Size'], df['Divide-and-Conquer Speedup'], label='Divide-and-Conquer Speedup', color='blue', marker='o', markersize=8, linestyle='-', linewidth=2)

# Format x-axis labels as powers of 10 for the speedup plot
axes[1].set_xticks(df['Input Size'])
axes[1].set_xticklabels([f"$10^{int(np.log10(i))}$" for i in df['Input Size']])

# Set y-axis to be in scientific notation for speedup plot
axes[1].yaxis.set_major_formatter(ScalarFormatter('e'))
axes[1].ticklabel_format(axis='y', style='sci', scilimits=(-4, -3))

# Speedup Plot Settings
axes[1].set_xlabel('Input Size', fontsize=14)
axes[1].set_ylabel('Speedup', fontsize=14)
axes[1].set_title('Speedup Plot (Blue with Dots)', fontsize=16)
axes[1].legend(fontsize=12)
axes[1].grid(linestyle='--', alpha=0.7)

# Adjust Layout and Save
output_image_path = os.path.join(BASE_DIR, '../../images/sequential_vs_anti_diagonal_combined.png')
plt.tight_layout()
plt.savefig(output_image_path)
plt.close()
