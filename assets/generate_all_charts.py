#!/usr/bin/env python3
"""
=============================================================================
CHART GENERATION SUITE
Critical Mineral Separation Benchmark — Publication Graphics
=============================================================================

This script generates all publication-quality figures for the benchmark.
All charts are self-contained and do not require external data files.

OUTPUT FILES:
  - assets/images/separation_efficiency_curve.png (Stage count vs beta)
  - assets/images/binding_energy_comparison.png (PFAS binding energies)
  - assets/images/economic_impact.png (CapEx/OpEx reduction)

USAGE:
  pip install -r requirements.txt
  python3 assets/generate_all_charts.py

=============================================================================
"""

import numpy as np
import os
import sys

# Ensure matplotlib uses a non-interactive backend for server/CI environments
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from matplotlib.lines import Line2D

# =============================================================================
# CONFIGURATION
# =============================================================================

# Output directory (absolute path for reliability)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, 'images')

# Style configuration
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 14,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.1,
})

# Color palette (colorblind-friendly)
COLORS = {
    'genesis': '#2E7D32',      # Dark green
    'standard': '#C62828',     # Dark red
    'neutral': '#424242',      # Dark gray
    'highlight': '#1565C0',    # Blue
    'warning': '#F57C00',      # Orange
    'background': '#FAFAFA',   # Light gray
}


# =============================================================================
# KREMSER EQUATION
# =============================================================================

def kremser_stages(beta, x_p=0.999, x_f=0.10):
    """Calculate theoretical stages using Kremser equation."""
    if beta <= 1.0:
        return float('inf')
    separation_degree = (x_p * (1 - x_f)) / (x_f * (1 - x_p))
    return np.log(separation_degree) / np.log(beta)


# =============================================================================
# FIGURE 1: SEPARATION EFFICIENCY CURVE
# =============================================================================

def generate_separation_efficiency_chart():
    """
    Generate the primary figure: Stage count vs. separation factor.
    
    This chart is the "hero image" for the repository, showing the dramatic
    reduction in required stages when using high-selectivity ligands.
    """
    
    print("Generating Figure 1: Separation Efficiency Curve...")
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # X-axis: separation factor (log scale)
    beta_values = np.logspace(0, 5, 1000)  # 1 to 100,000
    
    # Calculate stages for each beta
    stages = np.array([kremser_stages(b) for b in beta_values])
    
    # Plot the curve
    ax.plot(beta_values, stages, 
            color=COLORS['neutral'], linewidth=2.5, 
            label='Kremser Equation')
    
    # Mark P507 (standard)
    beta_p507 = 2.5
    stages_p507 = kremser_stages(beta_p507)
    ax.scatter([beta_p507], [stages_p507], 
               color=COLORS['standard'], s=200, zorder=5,
               marker='o', edgecolor='white', linewidth=2)
    ax.annotate(f'P507 (Industrial)\nβ = {beta_p507}\n{stages_p507:.0f} stages',
                xy=(beta_p507, stages_p507),
                xytext=(10, stages_p507 + 30),
                fontsize=11, fontweight='bold',
                color=COLORS['standard'],
                arrowprops=dict(arrowstyle='->', color=COLORS['standard'],
                               connectionstyle='arc3,rad=0.2'))
    
    # Mark Janus Ligand (Genesis)
    beta_genesis = 11000
    stages_genesis = kremser_stages(beta_genesis)
    ax.scatter([beta_genesis], [stages_genesis], 
               color=COLORS['genesis'], s=250, zorder=5,
               marker='*', edgecolor='white', linewidth=2)
    ax.annotate(f'Janus Ligand (Genesis)\nβ = {beta_genesis:,}\n{stages_genesis:.1f} stages',
                xy=(beta_genesis, stages_genesis),
                xytext=(1500, 25),
                fontsize=11, fontweight='bold',
                color=COLORS['genesis'],
                arrowprops=dict(arrowstyle='->', color=COLORS['genesis'],
                               connectionstyle='arc3,rad=-0.2'))
    
    # Add horizontal line at practical threshold
    ax.axhline(y=10, color=COLORS['highlight'], linestyle='--', 
               alpha=0.7, linewidth=1.5)
    ax.text(1.5, 11, 'Practical threshold (~10 stages)', 
            fontsize=9, color=COLORS['highlight'], style='italic')
    
    # Add vertical arrow showing improvement
    arrow_x = 100
    ax.annotate('', xy=(arrow_x, 5), xytext=(arrow_x, 75),
                arrowprops=dict(arrowstyle='<->', color=COLORS['warning'],
                               linewidth=2, mutation_scale=20))
    ax.text(arrow_x * 1.5, 35, 'Genesis\nAdvantage',
            fontsize=10, fontweight='bold', color=COLORS['warning'],
            ha='left', va='center')
    
    # Formatting
    ax.set_xscale('log')
    ax.set_xlabel('Separation Factor (β)', fontweight='bold')
    ax.set_ylabel('Theoretical Stages (N)', fontweight='bold')
    ax.set_title('Rare Earth Separation Efficiency: Stages vs. Selectivity\n'
                 'Target: 99.9% Nd from 10% Feed (Magnet Scrap)', 
                 fontweight='bold', fontsize=14)
    
    ax.set_xlim(1, 100000)
    ax.set_ylim(0, 200)
    
    ax.grid(True, alpha=0.3, which='both')
    ax.set_axisbelow(True)
    
    # Add footnote
    fig.text(0.02, 0.02, 
             'Source: Kremser-Brown-Souders equation. P507 β from Gupta & Krishnamurthy (2005). '
             'Genesis β from DFT (73 calculations, conservative cap at 11,000).',
             fontsize=8, style='italic', color='gray',
             transform=fig.transFigure)
    
    # Save
    output_path = os.path.join(OUTPUT_DIR, 'separation_efficiency_curve.png')
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    fig.savefig(output_path, facecolor='white', edgecolor='none')
    plt.close(fig)
    
    print(f"  ✓ Saved: {output_path}")
    return output_path


# =============================================================================
# FIGURE 2: PFAS BINDING ENERGY COMPARISON
# =============================================================================

def generate_binding_energy_chart():
    """
    Generate Figure 2: Binding energy comparison for PFAS adsorbents.
    """
    
    print("Generating Figure 2: PFAS Binding Energy Comparison...")
    
    # Data
    adsorbents = ['GAC\n(Standard)', 'Ion Exchange\n(Better)', 
                  'FC-8\n(Genesis)']
    binding_energies = [-45, -60, -121]  # kJ/mol
    colors = [COLORS['standard'], COLORS['warning'], COLORS['genesis']]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Bar chart
    bars = ax.bar(adsorbents, [abs(e) for e in binding_energies], 
                  color=colors, edgecolor='white', linewidth=2)
    
    # Add threshold line
    threshold = 80
    ax.axhline(y=threshold, color=COLORS['highlight'], linestyle='--', 
               linewidth=2, label=f'-80 kJ/mol threshold')
    ax.text(2.5, threshold + 2, 'Thermodynamic\nirreversibility\nthreshold',
            fontsize=9, color=COLORS['highlight'], ha='center', va='bottom')
    
    # Add value labels on bars
    for bar, energy in zip(bars, binding_energies):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 3,
                f'{energy} kJ/mol', ha='center', va='bottom',
                fontsize=11, fontweight='bold')
    
    # Add annotations
    ax.annotate('Leaches\n(fails EPA limit)', 
                xy=(0, 45), xytext=(0.3, 100),
                fontsize=9, color=COLORS['standard'],
                arrowprops=dict(arrowstyle='->', color=COLORS['standard']),
                ha='center')
    
    ax.annotate('Permanent\ncapture', 
                xy=(2, 121), xytext=(2.3, 80),
                fontsize=9, color=COLORS['genesis'],
                arrowprops=dict(arrowstyle='->', color=COLORS['genesis']),
                ha='center')
    
    # Formatting
    ax.set_ylabel('|Binding Energy| (kJ/mol)', fontweight='bold')
    ax.set_title('PFAS Adsorbent Performance: Binding Energy Comparison\n'
                 'Higher = Stronger Binding = Longer Retention',
                 fontweight='bold', fontsize=13)
    ax.set_ylim(0, 150)
    
    ax.legend(loc='upper left')
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_axisbelow(True)
    
    # Footnote
    fig.text(0.02, 0.02,
             'Source: DFT calculations (CP2K, PBE-D3(BJ)). '
             'GAC/IX values are literature estimates. '
             'FC-8 is lead Fluorocatcher candidate.',
             fontsize=8, style='italic', color='gray',
             transform=fig.transFigure)
    
    # Save
    output_path = os.path.join(OUTPUT_DIR, 'binding_energy_comparison.png')
    fig.savefig(output_path, facecolor='white', edgecolor='none')
    plt.close(fig)
    
    print(f"  ✓ Saved: {output_path}")
    return output_path


# =============================================================================
# FIGURE 3: ECONOMIC IMPACT ANALYSIS
# =============================================================================

def generate_economic_impact_chart():
    """
    Generate Figure 3: Economic impact comparison (CapEx/OpEx).
    """
    
    print("Generating Figure 3: Economic Impact Analysis...")
    
    # Data
    # Note: For Nd/Fe separation specifically (the Janus Ligand target),
    # P507 at β=2.5 requires ~10 theoretical stages (not 76-100 which applies
    # to full REE refineries separating adjacent lanthanides like Nd/Pr).
    categories = ['CapEx\n($M)', 'OpEx\n($M/yr)', 'Footprint\n(m²)', 'Stages']
    standard_values = [7.5, 1.5, 1000, 10]  # P507 baseline (Nd/Fe separation)
    genesis_values = [0.75, 0.15, 100, 1]   # Genesis Janus Ligand
    
    # Normalize to percentages (P507 = 100%)
    standard_pct = [100] * len(categories)
    genesis_pct = [(g/s)*100 for g, s in zip(genesis_values, standard_values)]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(11, 6))
    
    x = np.arange(len(categories))
    width = 0.35
    
    # Bars
    bars1 = ax.bar(x - width/2, standard_pct, width, 
                   label='P507 (Standard)', color=COLORS['standard'],
                   edgecolor='white', linewidth=2)
    bars2 = ax.bar(x + width/2, genesis_pct, width,
                   label='Janus Ligand (Genesis)', color=COLORS['genesis'],
                   edgecolor='white', linewidth=2)
    
    # Add value labels
    for bar, val in zip(bars1, standard_values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'{val:,}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    for bar, val, pct in zip(bars2, genesis_values, genesis_pct):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                f'{val:,}\n({pct:.0f}%)', ha='center', va='bottom', 
                fontsize=9, fontweight='bold', color=COLORS['genesis'])
    
    # Add reduction annotations
    for i, (s, g) in enumerate(zip(standard_values, genesis_values)):
        reduction = (1 - g/s) * 100
        mid_height = (100 + genesis_pct[i]) / 2
        ax.annotate(f'-{reduction:.0f}%',
                    xy=(i, mid_height), fontsize=12, fontweight='bold',
                    color=COLORS['warning'], ha='center', va='center',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                             edgecolor=COLORS['warning'], alpha=0.9))
    
    # Formatting
    ax.set_ylabel('Relative Value (P507 = 100%)', fontweight='bold')
    ax.set_title('Economic Impact: Janus Ligand vs. P507\n'
                 'REE Separation Plant (1,000 tonne/year capacity)',
                 fontweight='bold', fontsize=13)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 130)
    
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_axisbelow(True)
    
    # Footnote
    fig.text(0.02, 0.02,
             'Estimates based on stage count reduction. Actual values depend on '
             'site-specific factors. CapEx includes mixers, settlers, piping, instrumentation.',
             fontsize=8, style='italic', color='gray',
             transform=fig.transFigure)
    
    # Save
    output_path = os.path.join(OUTPUT_DIR, 'economic_impact.png')
    fig.savefig(output_path, facecolor='white', edgecolor='none')
    plt.close(fig)
    
    print(f"  ✓ Saved: {output_path}")
    return output_path


# =============================================================================
# FIGURE 4: SUPPLY CHAIN RISK MAP
# =============================================================================

def generate_supply_chain_chart():
    """
    Generate Figure 4: Supply chain concentration risk visualization.
    """
    
    print("Generating Figure 4: Supply Chain Risk Map...")
    
    # Data
    stages = ['Mining', 'Processing', 'Oxide Separation', 'Magnet Production']
    concentration = [60, 85, 92, 94]  # % controlled by single nation
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Color gradient based on concentration
    colors = [plt.cm.Reds(c/100 * 0.7 + 0.3) for c in concentration]
    
    bars = ax.barh(stages, concentration, color=colors, 
                   edgecolor='white', linewidth=2)
    
    # Add percentage labels
    for bar, pct in zip(bars, concentration):
        ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
                f'{pct}%', va='center', fontsize=12, fontweight='bold')
    
    # Add danger threshold
    ax.axvline(x=50, color=COLORS['warning'], linestyle='--', linewidth=2)
    ax.text(52, 3.5, 'Strategic\nvulnerability\nthreshold', 
            fontsize=9, color=COLORS['warning'], va='center')
    
    # Formatting
    ax.set_xlabel('Single-Nation Control (%)', fontweight='bold')
    ax.set_title('Rare Earth Supply Chain Concentration Risk\n'
                 'Percentage Controlled by Single Nation-State',
                 fontweight='bold', fontsize=13)
    ax.set_xlim(0, 110)
    
    ax.grid(True, alpha=0.3, axis='x')
    ax.set_axisbelow(True)
    ax.invert_yaxis()
    
    # Footnote
    fig.text(0.02, 0.02,
             'Source: DOE Critical Materials Strategy (2023), Adamas Intelligence (2024). '
             'Processing includes ore concentration and acid digestion.',
             fontsize=8, style='italic', color='gray',
             transform=fig.transFigure)
    
    # Save
    output_path = os.path.join(OUTPUT_DIR, 'supply_chain_risk.png')
    fig.savefig(output_path, facecolor='white', edgecolor='none')
    plt.close(fig)
    
    print(f"  ✓ Saved: {output_path}")
    return output_path


# =============================================================================
# MAIN
# =============================================================================

def main():
    """Generate all charts for the benchmark repository."""
    
    print("=" * 60)
    print("CHART GENERATION SUITE")
    print("Critical Mineral Separation Benchmark")
    print("=" * 60)
    print()
    
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    
    # Generate all figures
    figures = []
    
    try:
        figures.append(generate_separation_efficiency_chart())
        figures.append(generate_binding_energy_chart())
        figures.append(generate_economic_impact_chart())
        figures.append(generate_supply_chain_chart())
    except Exception as e:
        print(f"\n❌ Error generating charts: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    print()
    print("=" * 60)
    print(f"SUCCESS: Generated {len(figures)} figures")
    print("=" * 60)
    
    for fig_path in figures:
        print(f"  • {os.path.basename(fig_path)}")
    
    print()
    print("These images are ready for embedding in the README.")
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
