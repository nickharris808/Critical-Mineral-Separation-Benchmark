#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import os

def plot_separation_efficiency():
    # Data Sources:
    # P507: Standard industrial extractant (PC88A/D2EHPA equivalent). Beta ~ 2.5.
    # Janus Ligand: Genesis Patent 5 (EH-DPA). Beta > 10,000.
    
    technologies = ['P507\n(Standard)', 'Janus Ligand\n(Genesis)']
    selectivity = [2.5, 11700] 
    stages = [100, 1]
    
    # Create output directory
    output_dir = os.path.join(os.path.dirname(__file__), 'images')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'separation_efficiency_curve.png')

    fig, ax1 = plt.subplots(figsize=(10, 7))
    
    # Bar chart for Separation Factor (Log Scale)
    color = '#1f77b4' # Muted blue
    ax1.set_xlabel('Extraction Technology', fontweight='bold', fontsize=12)
    ax1.set_ylabel('Separation Factor (Nd/Fe) [Log Scale]', color=color, fontweight='bold', fontsize=12)
    bars = ax1.bar(technologies, selectivity, color=color, alpha=0.7, width=0.5, edgecolor='black')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_yscale('log')
    ax1.grid(True, which="both", ls="-", alpha=0.2)
    
    # Add value labels for bars
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height * 1.2,
                f'β ≈ {int(height)}',
                ha='center', va='bottom', color=color, fontweight='bold', fontsize=11)

    # Line chart for Stages Required
    ax2 = ax1.twinx()  
    color = '#d62728' # Muted red
    ax2.set_ylabel('Mixer-Settler Stages Required (99.9% Purity)', color=color, fontweight='bold', fontsize=12)
    ax2.plot(technologies, stages, color=color, marker='o', linewidth=3, markersize=12, label='Stages')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, 120)
    
    # Add value labels for line
    for i, v in enumerate(stages):
        ax2.text(i, v + 8, f'{v} Stages', ha='center', color=color, fontweight='bold', fontsize=11)

    plt.title('Magnet Recycling Efficiency Benchmark\nSeparation Factor vs. Process Complexity', fontsize=14, fontweight='bold', pad=20)
    
    # Add footnote
    plt.figtext(0.5, 0.02, "Source: Genesis Internal DFT & Lab Data vs. Standard P507 Literature Values", 
                ha="center", fontsize=8, style='italic')
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    print(f"Generated chart at: {output_path}")

if __name__ == "__main__":
    plot_separation_efficiency()
