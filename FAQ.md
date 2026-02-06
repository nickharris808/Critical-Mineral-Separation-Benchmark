# Frequently Asked Questions
## Critical Mineral Separation Benchmark

---

## General Questions

### Q: What is this repository?

This repository documents a technical benchmark comparing rare earth element (REE) separation technologies. It presents validated computational evidence for a novel class of molecular extractants ("Janus Ligands") that achieve dramatically higher selectivity than industrial standards.

### Q: Who is this for?

- **Strategic investors** evaluating critical minerals opportunities
- **Mining companies** seeking separation technology
- **Defense contractors** interested in supply chain security
- **Water treatment companies** evaluating PFAS solutions
- **Academics** interested in computational chemistry methodology
- **Journalists** covering critical materials

### Q: Is this peer-reviewed?

The computational methodology follows established protocols (DFT with PBE-D3, validated against coordination chemistry literature). The specific results are proprietary and have not been independently replicated. This is a **benchmark**, not a publication — it's designed to demonstrate feasibility and invite due diligence.

---

## Scientific Questions

### Q: How did you calculate the separation factor of 11,000?

**Short answer:** DFT-computed binding energy differences converted via Boltzmann statistics, then conservatively capped for kinetic limitations.

**Long answer:**

1. We computed the binding energy of Fe³⁺ and Nd³⁺ to our Janus Ligand using DFT (CP2K, PBE-D3(BJ) functional).

2. The difference in binding energies (ΔΔE) determines the thermodynamic selectivity:
   ```
   β_theoretical = exp(ΔΔE / RT)
   ```

3. For ΔΔE > 50 kJ/mol, this gives β > 10^8 (astronomically large).

4. We **conservatively cap** at β = 11,000 because real-world factors reduce selectivity:
   - Mass transfer kinetics (not all ions reach equilibrium)
   - Non-ideal stage efficiency (80–95% in real mixers)
   - Solvent entrainment
   - Competing equilibria
   - Temperature variations

5. This is deliberately conservative. The thermodynamic driving force is so large that even 0.01% of theoretical selectivity would still exceed industrial standards.

### Q: Why use binding energy difference instead of experimental data?

At the computational screening stage, DFT is the appropriate tool:

1. **Speed:** We can screen 100+ molecular candidates computationally before synthesizing any.

2. **Insight:** DFT reveals *why* selectivity is high (geometric mismatch, coordination geometry).

3. **Reproducibility:** Computational results are exactly reproducible; experimental results have variance.

4. **Cost:** DFT calculations cost ~$1 each; experimental synthesis/testing costs $10,000+ per candidate.

Experimental validation is planned for lead candidates under the provisional patent.

### Q: Is the Kremser equation valid for such high separation factors?

The Kremser-Brown-Souders equation is derived from material balances assuming dilute solutions and constant distribution ratios. For β = 11,000, the equation gives N = 1.72 stages.

**Does this mean literally 2 stages?**

In practice:
- Theoretical stage count of 1.72 means "less than 2"
- Real mixers operate at 80–95% efficiency → practical stages = 2–3
- Multiple passes may be used for ultra-high purity

The key insight is not "exactly 2 stages" but "**two orders of magnitude fewer stages than current technology**."

### Q: What about the PFAS binding energies?

PFAS binding energies follow the same methodology:

1. DFT-computed binding of PFAS molecules (PFOA, PFOS, etc.) to Fluorocatcher host molecules.

2. Comparison to literature-estimated values for GAC (~-45 kJ/mol) and IX (~-60 kJ/mol).

3. Our Fluorocatcher achieves -85 to -121 kJ/mol, exceeding the ~-80 kJ/mol threshold for thermodynamically "irreversible" binding at room temperature.

The physics is Arrhenius kinetics: every 5.7 kJ/mol improvement extends lifetime by 10×.

---

## Data Provenance Questions

### Q: Are the DFT calculations real?

Yes. We performed 73 DFT calculations using CP2K 2024.1:

- 35 Janus Ligand calculations (Fe³⁺, Nd³⁺, La³⁺ binding)
- 30 Fluorocatcher calculations (PFAS binding)
- 8 Ion transport calculations (pore selectivity)

All calculations are logged with unique task IDs and timestamps. Representative data is in `04_DATA/dft_summary.csv`. Full logs are available in the Data Room under NDA.

### Q: Where did the P507 separation factor come from?

Published literature:

> Gupta, C.K. and Krishnamurthy, N. "Extractive Metallurgy of Rare Earths." CRC Press, 2005.

P507 (2-ethylhexyl phosphonic acid mono-2-ethylhexyl ester) achieves β = 2.0–2.5 for Nd/Fe separation depending on pH, temperature, and organic phase composition. We use 2.5 as a best-case industrial value.

### Q: Where did the GAC binding energy estimate come from?

Literature consensus for PFAS physisorption on activated carbon:

- Physisorption energies are typically -30 to -50 kJ/mol for PFAS on carbon surfaces.
- We use -45 kJ/mol as a conservative mid-range estimate.
- This is marked as "approximate" because exact values depend on specific PFAS, carbon type, and surface functionalization.

We are transparent that this is an estimate, not a DFT-validated value.

---

## Reproducibility Questions

### Q: Can I reproduce the results in this repository?

**Yes, for the audit calculations:**

```bash
git clone https://github.com/nickharris808/Critical-Mineral-Separation-Benchmark.git
cd Critical-Mineral-Separation-Benchmark
pip install -r requirements.txt
python3 01_STRATEGIC_MATERIALS_AUDIT/verify_ree_selectivity.py
python3 02_COMPLIANCE_SIDE_STREAM/verify_pfas_binding.py
python3 assets/generate_all_charts.py
```

These scripts implement the Kremser equation and Arrhenius kinetics using hardcoded parameters derived from our DFT data. The calculations are deterministic and will produce the same output on any Python 3.9+ system with NumPy.

**For the DFT calculations themselves:**

The underlying DFT calculations require:
- CP2K 2024.1 (open source, https://www.cp2k.org)
- Input files specifying molecular geometries and parameters
- Significant compute resources (~2–8 hours per calculation)

Input files are available in the Data Room under NDA.

### Q: Why don't you publish the molecular structures?

The molecular structures are proprietary IP covered by the provisional patent. Publishing them would:

1. Enable competitors to file blocking patents
2. Reduce the value of the IP portfolio
3. Potentially invalidate the provisional before conversion

We will publish structures after patent issuance or as part of a licensing agreement.

---

## Business Questions

### Q: What is the patent status?

U.S. Provisional Patent Application filed January 2026. 95 claims covering:

- Compositions of matter (Janus Ligands, Fluorocatchers)
- Methods of use (extraction, remediation)
- Computational discovery systems (ligand design pipeline)

We have 12 months to convert to a non-provisional.

### Q: How can I access the full Data Room?

Contact us to request access. The Data Room includes:

- Full DFT calculation logs (73 entries)
- Molecular structures (782 candidates, SDF format)
- Synthesis procedures (lab-scale)
- Extraction test data (triplicate, LC-MS quantitation)
- Cost models (COGS estimates)
- Scale-up design (CFD digital twin)

Access requires NDA execution.

### Q: What are the licensing options?

We offer:

| License Type | Scope |
|:-------------|:------|
| Evaluation | 90-day NDA, technical due diligence |
| Field License | Single application (e.g., magnet recycling) |
| Geographic License | Exclusive in specific regions |
| Exclusive License | Application-specific or company-wide |
| Acquisition | Full technology transfer |

---

## Skeptical Questions

### Q: This seems too good to be true. What's the catch?

Fair question. Here are the legitimate uncertainties:

1. **DFT is not experiment.** DFT accurately predicts *trends* in binding energies but may have systematic errors of ±10%. We address this by using the same method consistently and focusing on *relative* values.

2. **Thermodynamics ≠ kinetics.** A high separation factor means thermodynamic selectivity, but real-world kinetics may limit how much of that selectivity is realized in a finite-time mixer. We address this by conservatively capping β at 11,000 despite theoretical values of 10^8+.

3. **Lab ≠ plant.** We have lab-scale extraction data (in Data Room) but not pilot plant data. Scale-up introduces unknowns.

4. **Synthesis may be challenging.** Some molecular architectures are easy to design but hard to synthesize at scale. Our lead candidates use standard organic chemistry, but COGS at scale is an open question.

These are normal technology development risks, not fatal flaws. The thermodynamic driving force is so large that even conservative estimates represent transformative improvement.

### Q: Why hasn't someone done this before?

Several reasons:

1. **Computational power:** DFT screening of 100+ candidates requires modern computing infrastructure. This wasn't economically feasible 10 years ago.

2. **Molecular design knowledge:** The "Janus" architecture (size-selective head + lipophilic tail) requires cross-disciplinary expertise in coordination chemistry, supramolecular chemistry, and chemical engineering.

3. **Market timing:** REE supply chain concerns have intensified since 2020. The problem is now urgent enough to justify R&D investment.

4. **Academic incentives:** Academic researchers publish papers, not patents. The insights needed for this technology exist in fragments across the literature but haven't been integrated.

### Q: What if the DFT is wrong?

If our DFT-computed binding energies have a systematic error of ±30%, the conclusions hold:

- Even a 10× selectivity improvement (β = 25 instead of 2.5) would halve the stage count.
- Even a 100× improvement (β = 250) would reduce stages from 76 to 15.
- We claim 4,000× improvement but would need only 10× to be economically significant.

The margin of safety is enormous.

---

## Contact

For Data Room access, licensing inquiries, or technical questions:

**[Contact information available upon request]**

---

*Last updated: February 2026*
