import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Colors for plotting
colors = {
    'Sequential': '#1f77b4',
    'Anti-Diagnoal': '#ff7f0e',
    'Divide-and-Conquer': '#2ca02c'
}

# Load Data
data_path = os.path.join(BASE_DIR, '../../databases/sequential_vs_divide_and_conquer/results.csv')
df = pd.read_csv(data_path)

# Create Figure
fig, axes = plt.subplots(1, 2, figsize=(22, 10))

# Bar Plot: Sequential vs Divide-and-Conquer
x = np.arange(len(df['Input Size']))
width = 0.35
axes[0].bar(x - width / 2, df['Sequential Time (s)'], width, label='Sequential', color=colors['Sequential'])
axes[0].bar(x + width / 2, df['Divide-and-Conquer Time (s)'], width, label='Divide-and-Conquer', color=colors['Divide-and-Conquer'])

# Bar Plot Settings
axes[0].set_xticks(x)
axes[0].set_xticklabels(df['Input Size'], rotation=45, fontsize=12)
axes[0].set_xlabel('Input Size', fontsize=14)
axes[0].set_ylabel('Time (s)', fontsize=14)
axes[0].set_title('Time Taken: Sequential vs Divide-and-Conquer (Bar Graph)', fontsize=16)
axes[0].legend(fontsize=12)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Annotate Bars (Check for finite values)
for i in range(len(df['Input Size'])):
    # Check if values are finite before annotating
    if np.isfinite(df['Sequential Time (s)'][i]):
        axes[0].text(i - width / 2, df['Sequential Time (s)'][i] + 0.1, 
                     f"{df['Sequential Time (s)'][i]:.2f}", ha='center', fontsize=10)
    if np.isfinite(df['Divide-and-Conquer Time (s)'][i]):
        axes[0].text(i + width / 2, df['Divide-and-Conquer Time (s)'][i] + 0.1, 
                     f"{df['Divide-and-Conquer Time (s)'][i]:.2f}", ha='center', fontsize=10)

# Line Plot: Divide-and-Conquer
axes[1].plot(df['Input Size'], df['Divide-and-Conquer Time (s)'], label='Divide-and-Conquer', color=colors['Divide-and-Conquer'], marker='s', markersize=8, linewidth=2)

# Line Plot Settings
axes[1].set_xlabel('Input Size', fontsize=14)
axes[1].set_ylabel('Time (s)', fontsize=14)
axes[1].set_title('Divide-and-Conquer (Line Plot)', fontsize=16)
axes[1].legend(fontsize=12)
axes[1].grid(linestyle='--', alpha=0.7)

# Adjust Layout and Save
output_image_path = os.path.join(BASE_DIR, '../../images/sequential_vs_divide_and_conquer.png')
plt.tight_layout()
plt.savefig(output_image_path)
plt.close()
