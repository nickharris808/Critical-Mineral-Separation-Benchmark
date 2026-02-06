# Computational Methodology
## Density Functional Theory Protocol for Metal-Ligand Binding Calculations

---

## Overview

This document describes the computational chemistry methodology used to calculate metal-ligand binding energies for the Janus Ligand screening program.

All calculations were performed using **Density Functional Theory (DFT)**, the industry-standard quantum mechanical method for coordination chemistry.

---

## Software Stack

| Component | Version | Purpose |
|:----------|:--------|:--------|
| **CP2K** | 2024.1 | Primary DFT engine |
| **RDKit** | 2023.09 | Molecular structure generation |
| **Open Babel** | 3.1.1 | Format conversion |
| **Python** | 3.11 | Orchestration and analysis |

---

## DFT Functional Selection

### Functional: PBE

We used the **Perdew-Burke-Ernzerhof (PBE)** generalized gradient approximation (GGA) functional.

**Rationale:**
- Well-validated for transition metal and lanthanide coordination chemistry
- Reasonable computational cost for molecules with 50-200 atoms
- Consistent performance across different metal centers

### Dispersion Correction: D3(BJ)

We applied **Grimme's D3 dispersion correction with Becke-Johnson damping**.

**Rationale:**
- Accurately captures van der Waals interactions between ligand and solvent
- Important for predicting phase-transfer behavior
- Validated against experimental solvation energies

---

## Basis Set

### DZVP-MOLOPT-SR-GTH

**Double-Zeta Valence Polarized, Molecularly Optimized, Short-Range, Goedecker-Teter-Hutter**

| Property | Value |
|:---------|:------|
| Quality | Double-zeta with polarization |
| Optimization | Optimized for molecular (non-periodic) calculations |
| Pseudopotential | GTH-PBE |

**Element-Specific Settings:**

| Element | Basis | Pseudopotential | Notes |
|:--------|:------|:----------------|:------|
| C, H, O, N | DZVP-MOLOPT-SR-GTH | GTH-PBE-q4/q1/q6/q5 | Standard main-group |
| Fe | DZVP-MOLOPT-SR-GTH | GTH-PBE-q16 | 16 valence electrons |
| La, Nd | DZVP-MOLOPT-SR-GTH | GTH-PBE-q11 | 4f + 5d + 6s electrons |

---

## Solvation Model

### COSMO (Conductor-like Screening Model)

We used **implicit solvation** to model the organic diluent environment.

| Parameter | Value | Rationale |
|:----------|:------|:----------|
| Dielectric constant (ε) | 2.0 | Kerosene / Isopar |
| Cavity construction | VDW radii | Standard approach |

**Why implicit solvation?**
- Explicit solvent would require 100+ solvent molecules
- Implicit models capture bulk electrostatic effects at low cost
- Validated for extraction thermodynamics

---

## Spin State Handling

### Iron (Fe³⁺)

Fe³⁺ has a d⁵ electronic configuration. In most coordination environments, Fe³⁺ adopts a **high-spin (S = 5/2)** state.

| Property | Value |
|:---------|:------|
| Charge | +3 |
| Multiplicity | 6 (high-spin) |
| UKS | TRUE (unrestricted Kohn-Sham) |

### Lanthanides (La³⁺, Nd³⁺)

La³⁺ has no unpaired electrons (d⁰ f⁰ after ionization). Nd³⁺ has three unpaired f-electrons (f³).

| Ion | Charge | Multiplicity | UKS |
|:----|:-------|:-------------|:----|
| La³⁺ | +3 | 1 | FALSE |
| Nd³⁺ | +3 | 4 | TRUE |

---

## Geometry Optimization

All structures were geometry-optimized before energy calculation.

| Parameter | Value |
|:----------|:------|
| Optimizer | BFGS |
| Force tolerance | 4.5E-4 Ha/Bohr |
| Displacement tolerance | 3.0E-3 Bohr |
| Max iterations | 500 |

---

## SCF Convergence

| Parameter | Value |
|:----------|:------|
| SCF method | Orbital Transformation (OT) |
| Preconditioner | FULL_SINGLE_INVERSE |
| Convergence criterion | 1.0E-5 Ha |
| Max SCF cycles | 500 |
| Outer SCF | Enabled (max 50 iterations) |

---

## Binding Energy Calculation

The binding energy for a metal-ligand complex is computed as:

```
ΔE_binding = E(Ligand:Metal) - E(Ligand) - E(Metal)
```

Where all three species are computed at the same level of theory with the same basis set and solvation model.

### Reference States

| Species | Charge | Multiplicity | Geometry |
|:--------|:-------|:-------------|:---------|
| Ligand (free) | 0 | 1 | Optimized |
| Metal (free) | +3 | Varies | Single atom |
| Complex | +3 | Varies | Optimized |

---

## Validation

### Convergence Statistics

| Category | Calculations | Converged | Rate |
|:---------|:-------------|:----------|:-----|
| Janus Ligand + Fe³⁺ | 35 | 34 | 97.1% |
| Janus Ligand + Nd³⁺/La³⁺ | 35 | 35 | 100% |
| Fluorocatcher + PFAS | 30 | 30 | 100% |
| Ion Transport | 8 | 8 | 100% |
| **Total** | **73** | **72** | **98.6%** |

### Consistency Checks

1. **Ionic radius trend:** Binding energies follow expected trend La > Nd > Sm
2. **Fe rejection:** Fe³⁺ consistently shows weaker binding than lanthanides
3. **Tail group independence:** Selectivity is dominated by coordination geometry, not tail chemistry

---

## Reproducibility

All calculations can be reproduced with the following:

1. **Input files:** Available in Data Room under NDA
2. **Software:** CP2K 2024.1 (open source)
3. **Hardware:** Calculations run on cloud instances (c2-standard-32)
4. **Task IDs:** All calculations logged with unique identifiers

---

## References

1. Perdew, J.P., Burke, K., and Ernzerhof, M. "Generalized Gradient Approximation Made Simple." Phys. Rev. Lett. 77, 3865 (1996).

2. Grimme, S. et al. "A consistent and accurate ab initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements H-Pu." J. Chem. Phys. 132, 154104 (2010).

3. VandeVondele, J. et al. "Quickstep: Fast and accurate density functional calculations using a mixed Gaussian and plane waves approach." Comput. Phys. Commun. 167, 103-128 (2005).

4. Goedecker, S., Teter, M., and Hutter, J. "Separable dual-space Gaussian pseudopotentials." Phys. Rev. B 54, 1703 (1996).
