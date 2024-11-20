import pandas as pd
import matplotlib.pyplot as plt

def create_performance_plots():
    df = pd.read_excel('lcs_results.xlsx')
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    ax1.semilogx(df['Input Size'], df['Speedup'], 'b-o', linewidth=2, markersize=8)
    ax1.grid(True)
    ax1.set_xlabel('Input Size')
    ax1.set_ylabel('Speedup (Sequential/Parallel)')
    ax1.set_title('Speedup vs Input Size')
    
    x = range(len(df['Input Size']))
    width = 0.35
    
    ax2.bar([i - width/2 for i in x], df['Sequential Time (s)'], width, 
            label='Sequential', color='blue', alpha=0.7)
    ax2.bar([i + width/2 for i in x], df['Parallel Time (s)'], width,
            label='Parallel', color='red', alpha=0.7)
    
    ax2.set_xticks(x)
    ax2.set_xticklabels(df['Input Size'], rotation=45)
    ax2.set_yscale('log')
    ax2.grid(True)
    ax2.set_xlabel('Input Size')
    ax2.set_ylabel('Time (seconds)')
    ax2.set_title('Sequential vs Parallel Execution Time')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('performance_comparison.png', dpi=300, bbox_inches='tight')
    print("Plots have been saved as 'performance_comparison.png'")

if __name__ == "__main__":
    create_performance_plots()